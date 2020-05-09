"""Codewars: Drying Potatoes
7 kyu

URL: https://www.codewars.com/kata/58ce8725c835848ad6000007/train/python

All we eat is water and dry matter.
John bought potatoes: their weight is 100 kilograms. Potatoes contain 
water and dry matter.
The water content is 99 percent of the total weight. He thinks they are 
too wet and puts them in an oven - at low temperature - for them to lose 
some water.
At the output the water content is only 98%.
What is the total weight in kilograms (water content plus dry matter) 
coming out of the oven?
He finds 50 kilograms and he thinks he made a mistake: 
"So much weight lost for such a small change in water content!"
Can you help him?
Write function potatoes with
int parameter p0 - initial percent of water-
int parameter w0 - initial weight -
int parameter p1 - final percent of water -
potatoesshould return the final weight coming out of the oven w1 
truncated as an int.

Example:
potatoes(99, 100, 98) --> 50
"""

def potatoes(p0, w0, p1):
    """
    - p1/100 = water1 / water1 + (1 - p0/100) * w0
      => water1 = w0 * p1/100 * (1 - p0/100) / (1 - p1/100)
    - dry = w0 * (1 - p0/100)
    - w1 = water1 + dry = w0 * (100 - p0) / (100 - p1)

    Example:
    98/100 = water1 / water1 + (1- 99/100) * 100
    water1 = 49
    w1 = 49 + 1 = 50
    """
    w1 = w0 * (100 - p0) / (100 - p1)
    return int(w1)


def main():
    # Output: 114
    p0, w0, p1 = 82, 127, 80
    print(potatoes(p0, w0, p1))


# def dotest(p0, w0, p1, exp):
# Test.assert_equals(potatoes(p0, w0, p1), exp)
# Test.describe("potatoes")
# Test.it("Basic tests")
# dotest(82, 127, 80, 114)
# dotest(93, 129, 91, 100)


if __name__ == '__main__':
    main()


