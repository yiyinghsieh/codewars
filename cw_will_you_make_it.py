"""Codewars: Will you make it?
8 kyu

URL: https://www.codewars.com/kata/5861d28f124b35723e00005e/train/python

Will you make it?
You were camping with your friends far away from home, but when it's time to go 
back, you realize that you fuel is running out and the nearest pump is 50 miles 
away! You know that on average, your car runs on about 25 miles per gallon. 
There are 2 gallons left. Considering these factors, write a function that 
tells you if it is possible to get to the pump or not. Function should return 
true (1 in Prolog) if it is possible and false (0 in Prolog) if not. The input 
values are always positive.
"""


from __future__ import division
from __future__ import print_function


def zero_fuel(distance_to_pump, mpg, fuel_left):
    if mpg * fuel_left >= distance_to_pump:
        return True
    else:
        return False


def main():
    # # Output: True
    # distance_to_pump = 50
    # mpg = 25
    # fuel_left = 2
    # print(zero_fuel(distance_to_pump, mpg, fuel_left))

    # # Output: False
    # distance_to_pump = 100
    # mpg = 50
    # fuel_left = 1
    # print(zero_fuel(distance_to_pump, mpg, fuel_left))


    assert zero_fuel(50, 25, 2) == True
    assert zero_fuel(100, 50, 1) == False


if __name__ == '__main__':
    main()

