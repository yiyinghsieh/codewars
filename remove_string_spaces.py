"""Codewars: Remove String Spaces
8 kyu

URL: https://www.codewars.com/kata/remove-string-spaces/train/python

Simple, remove the spaces from the string, then return the resultant string.

Test.describe("Basic tests")
Test.assert_equals(no_space('8 j 8   mBliB8g  imjB8B8  jl  B'), '8j8mBliB8gimjB8B8jlB')
Test.assert_equals(no_space('8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd'), '88Bifk8hB8BB8BBBB888chl8BhBfd')
Test.assert_equals(no_space('8aaaaa dddd r     '), '8aaaaaddddr')
Test.assert_equals(no_space('jfBm  gk lf8hg  88lbe8 '), 'jfBmgklf8hg88lbe8') 
Test.assert_equals(no_space('8j aam'), '8jaam')
"""

from __future__ import division
from __future__ import print_function


def no_space_iter(x):
    # Iterate through chars in x, append it if not space.
    string = []
    for c in x:
        if c != ' ':
            string.append(c)
    return ''.join(string)


def no_space_split(x):
    # Split x by space, and then join char list.
    return ''.join(x.split())


def no_space_replace(x):
    # Replace space.
    return x.replace(' ', '')


def main():
    import time
    # Output: "8j8mBliB8gimjB8B8jlB" 
    x = '8 j 8   mBliB8g  imjB8B8  jl  B'

    start_time = time.time()
    print('By iter:', no_space_iter(x))
    print('Time:', time.time() - start_time)

    start_time = time.time()
    print('By split:', no_space_split(x))
    print('Time:', time.time() - start_time)

    start_time = time.time()
    print('By replace:', no_space_replace(x))
    print('Time:', time.time() - start_time)

    # Output: "I88Bifk8hB8BB8BBBB888chl8BhBfd" 
    x = '8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd'

    start_time = time.time()
    print('By iter:', no_space_iter(x))
    print('Time:', time.time() - start_time)

    start_time = time.time()
    print('By split:', no_space_split(x))
    print('Time:', time.time() - start_time)

    start_time = time.time()
    print('By replace:', no_space_replace(x))
    print('Time:', time.time() - start_time)


if __name__ == '__main__':
    main()

