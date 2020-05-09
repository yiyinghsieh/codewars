"""Codewars: Draw stairs
8 kyu

URL: https://www.codewars.com/kata/draw-stairs/

Given a number n, draw stairs using the letter "I", n tall and n wide, with the tallest
in the top left.

For example n = 3 result in "I\n I\n I", or printed:
I
 I
  I

Another example, a 7-step stairs should be drawn like this:
I
 I
  I
   I
    I
     I
      I
"""

from __future__ import division
from __future__ import print_function


def draw_stairs(n):
    stairs = []
    for i in range(n):
        stairs.append(' ' * i)
        stairs.append('I')
        if i != (n - 1):
            stairs.append('\n')

    return ''.join(stairs)

        
def main():
    # Output: "I\n I\n I" 
    n = 3
    print(draw_stairs(n))

    # Output: "I\n I\n I\n   I\n    I\n     I\n      I\n       I" 
    n = 7
    print(draw_stairs(n))

    # n = int(input('Input n for stairs: '))
    # print(draw_stairs(n))


if __name__ == '__main__':
    main()
