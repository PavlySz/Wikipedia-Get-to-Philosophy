'''
Task: Given a Wikipedia link, crawl the first link till you get
      to the Philosophy page or get stuck in a loop.
Author: Pavly Salah

Clicking on the first non-parenthesized, non-italicized link
Ignoring external links, links to the current page, or red links (links to non-existent pages)
'''

import sys
import time
import urllib
import requests
from bs4 import BeautifulSoup


def find_first_link(url):
    '''
    Given a URL, get the first 'normal' link

    Args:
        url (str): a Wikipedia URL

    Returns:
        first_link (str): the first 'normal' link
    '''
    # Open the URL
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    # Get the body content
    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")

    # If the link contains no links it remains None
    article_link = None

    # Find all the direct children of content_div that are paragraphs
    for element in content_div.find_all("p", recursive=False):
        # Find only the direct children
        if element.find("a", recursive=False):
            article_link = element.find("a", recursive=False).get('href')
            break

    # If the page contains no links
    if not article_link:
        return None

    # Build a full url
    first_link = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)

    return first_link


def continue_scraping(visit_history, max_steps=50):
    '''
    Whether or not to continue scraping

    Args:
        visit_history (list of strings): list of visited pages
        max_steps (int): maximum number of pages to visit until the search stops

    Returns:
        bool: whether to continue the searching process or not
    '''
    target_url = "https://en.wikipedia.org/wiki/Philosophy"

    # If Philosophy page is reached
    if visit_history[-1] == target_url:
        print(visit_history)
        print(f"[SUCCESS] 'Philosphy' article reached after {len(visit_history)-1} hops!")
        return False

    # If maximum number of iterations is reached
    if len(visit_history) > max_steps:
        print("[FAIL] Maximum searches reached. Aborted.")
        return False

    # If the visited link has already been visited
    # I.e. will be stuck in a loop
    if visit_history[-1] in visit_history[:-1]:
        print(visit_history[-1])
        print("[FAIL] Stuck in a loop. Search aborted.")
        return False

    return True


def get_user_input():
    '''
    Get URL from user

    Returns:
        - Wikipedia URL
    '''
    # Default URL
    random_url = 'https://en.wikipedia.org/wiki/Special:Random'

    # If the user didn't specify a specific link, use the default one
    if len(sys.argv) == 1:
        user_url = random_url
        print(f'Using random URL: {random_url}')

    # If the user provided a link, use it
    else:
        user_url = sys.argv[1]

    # Make sure the user-provided link is an actual Wikipedia link
    # Can be improved using Regex [TBD]
    if not user_url.startswith('https://en.wikipedia.org/wiki/'):
        print('This is not a valid Wikipedia URL. Please try again.')
        print('A valid Wikipedia URL starts with `https://en.wikipedia.org/wiki/`')
        user_url = get_user_input()

    return user_url


def main():
    '''
    Main function
    - Get the user input.
    - Try to get to the Philosophy page
    - Abort if stuck in a loop or arive at a page with no links
    '''
    # Get URL from the user or use the default URL
    user_url = get_user_input()

    # store the visited pages
    visited_urls = [user_url]

    while continue_scraping(visited_urls):
        print(visited_urls[-1])

        first_link = find_first_link(visited_urls[-1])

        # In case a page has no links
        if not first_link:
            print("[FAIL] Arrived at an article with no links. Aborted!")
            break

        # Append the link to the list of visited links
        visited_urls.append(first_link)

        # Avoid overload
        time.sleep(0.5)


if __name__ == '__main__':
    main()
