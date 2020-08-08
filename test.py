'''
Test get_to_philosophy N times
'''
import subprocess

number_of_tests = 10
number_of_fails = 0

for i in range(number_of_tests):
    print(f'* Test number {i+1}')

    stdout = subprocess.check_output('python3 get_to_philosophy.py'.split()).decode('utf-8')
    last_output = stdout.split('\n')[-2]    # the very last output is an empty string [TO DEBUG]

    result = last_output.split()[0]
    print(f'\tTest result: {result}')
    if result == '[FAIL]':
        number_of_fails += 1

failure_ratio = number_of_fails / number_of_tests
print(f'Ran {number_of_tests} tests. Failure ratio = {failure_ratio}')
