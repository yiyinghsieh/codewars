"""Codewars: Watermelon
8 kyu

URL: https://www.codewars.com/kata/55192f4ecd82ff826900089e/train/python

It's too hot, and they can't even…
One hot summer day Pete and his friend Billy decided to buy watermelons. 
They chose the biggest crate. They rushed home, dying of thirst, and decided to 
divide their loot, however they faced a hard problem.

Pete and Billy are great fans of even numbers, that's why they want to divide 
the number of watermelons in such a way that each of the two parts consists of 
an even number of watermelons. However, it is not obligatory that the parts are 
qual.

Example: the boys can divide a stack of 8 watermelons into 2+6 melons, 
or 4+4 melons.

The boys are extremely tired and want to start their meal as soon as possible, 
that's why you should help them and find out, whether they can divide the fruits 
in the way they want. For sure, each of them should get a part of positive weight.

Task
Given an integral number of watermelons w (1 ≤ w ≤ 100; 1 ≤ w in Haskell), 
check whether Pete and Billy can divide the melons so that each of them gets 
an even amount.

Examples
divide(2) == false # 2 = 1 + 1
divide(3) == false # 3 = 1 + 2
divide(4) == true  # 4 = 2 + 2
divide(5) == false # 5 = 2 + 3
divide(6) == true  # 6 = 2 + 4
"""


from __future__ import division
from __future__ import print_function


def divide(weight):
    if weight == 2 or weight % 2 != 0:
        return False
    else:
        return True


def divide(weight):
    return weight != 2 and weight % 2 == 0

def main():
    # # Output: True 
    # weight = 4
    # print(divide(weight))
    # # Output: False 
    # weight = 5
    # print(divide(weight))
    # # Output: True 
    # weight = 6
    # print(divide(weight))

    assert divide(2) == False
    assert divide(4) == True
    assert divide(5) == False
    assert divide(6) == True
    assert divide(88) == True
    assert divide(100) == True
    assert divide(67) == False
    assert divide(90) == True
    assert divide(10) == True
    assert divide(99) == False
    assert divide(32) == True


if __name__ == '__main__':
    main()

