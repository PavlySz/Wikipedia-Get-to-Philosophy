# Wikipedia-Get-to-Philosophy

### Intro
Clicking on the first link in the main body of a Wikipedia article and repeating the process for subsequent articles would usually lead to the article Philosophy.
 
The program receives a Wikipedia link as an input, go to another normal link and repeat this process until either Philosophy page is reached, or we are in an article without any outgoing Wikilinks, or stuck in a loop.

### Dependecies:
- Urllib
- Beautiful Soup 4

### Sample output
- Failure case 1 (Arrive at a website with no links):

Using random URL: https://en.wikipedia.org/wiki/Special:Random

https://en.wikipedia.org/wiki/Greek_vase_painting

https://en.wikipedia.org/wiki/Ancient_Greece

https://en.wikipedia.org/wiki/Greek_language

[FAIL] Arrived at an article with no links. Aborted!


- Failure case 2 (stuck in a loop):
Using random URL: https://en.wikipedia.org/wiki/Special:Random

https://en.wikipedia.org/wiki/Glimmen

https://en.wikipedia.org/wiki/Netherlands

https://en.wikipedia.org/wiki/Dutch_language

https://en.wikipedia.org/wiki/West_Germanic_languages

https://en.wikipedia.org/wiki/Germanic_languages

https://en.wikipedia.org/wiki/Indo-European_languages

https://en.wikipedia.org/wiki/Language_family

https://en.wikipedia.org/wiki/Language

https://en.wikipedia.org/wiki/Grammar

https://en.wikipedia.org/wiki/Linguistics

https://en.wikipedia.org/wiki/Science

https://en.wikipedia.org/wiki/Latin

https://en.wikipedia.org/wiki/Classical_language

https://en.wikipedia.org/wiki/Language

[FAIL] Stuck in a loop. Search aborted.



- Success case (Got to Philosophy successfully):
Using random URL: https://en.wikipedia.org/wiki/Special:Random

https://en.wikipedia.org/wiki/Reggae

https://en.wikipedia.org/wiki/Music_genre

https://en.wikipedia.org/wiki/Music

https://en.wikipedia.org/wiki/The_arts#Music

https://en.wikipedia.org/wiki/Creativity

https://en.wikipedia.org/wiki/Idea

https://en.wikipedia.org/wiki/Philosophy
[SUCCESS] 'Philosphy' article reached after 7 hops!

