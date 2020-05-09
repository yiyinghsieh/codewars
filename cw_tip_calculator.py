"""Codewars: Tip Calculator
8 kyu

URL: https://www.codewars.com/kata/tip-calculator/train/python

based on the total amount of the bill and the service.

You need to consider the following ratings:

- Terrible: tip 0%
- Poor: tip 5%
- Good: tip 10%
- Great: tip 15%
- Excellent: tip 20%

The rating is case insensitive (so "great" = "GREAT"). 
If an unrecognised rating is received, then you need to return:
"Rating not recognised" in Javascript, Python and Ruby...
...or null in Java
...or -1 in C#
Because you're a nice person, you always round up the tip, 
regardless of the service.
Example:
Test.assert_equals(calculate_tip(30, "poor"), 2)
Test.assert_equals(calculate_tip(20, "Excellent"), 4)
Test.assert_equals(calculate_tip(20, "hi"), 'Rating not recognised')
Test.assert_equals(calculate_tip(107.65, "GReat"), 17)
Test.assert_equals(calculate_tip(20, "great!"), 'Rating not recognised')
"""


from __future__ import division
from __future__ import print_function


def calculate_tip(amount, rating):
    import math

    # Use dict: ratings(in lower case)->tipspercent, for random ratings.
    ratings_tipspercent = {
        'terrible': 0.0, 
        'poor': 5.0, 
        'good': 10.0,
        'great': 15.0,
        'excellent': 20.0
    }

    # Convert rating to lower case, same as dictionary's key.
    rating_lower = rating.lower()

    # Check if rating is in dict, calculate tips based on tips percent.
    if rating_lower in ratings_tipspercent:
        tips_raw = amount * ratings_tipspercent[rating_lower] / 100
        tips = math.ceil(tips_raw)
        return tips
    else:
        return 'Rating not recognised'
    

def main():
    # Output: 2
    amount, rating = 30, 'poor'
    print(calculate_tip(amount, rating))

    # Output: 4
    amount, rating = 20, 'Excellent'
    print(calculate_tip(amount, rating))

    # Output: 'Rating not recognised'
    amount, rating = 20, 'hi'
    print(calculate_tip(amount, rating))

    # Output: 17
    amount, rating = 107.65, 'GReat'
    print(calculate_tip(amount, rating))

    # Output: 'Rating not recognised'
    amount, rating = 20, 'great!'
    print(calculate_tip(amount, rating))

    # Output: 0
    amount, rating = 47, 'TERRIBle'
    print(calculate_tip(amount, rating))


if __name__ == '__main__':
    main()
