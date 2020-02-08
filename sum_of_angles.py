"""Sum of angles
7 kyu

URL: https://www.codewars.com/kata/5a03b3f6a1c9040084001765/train/python

Find the total sum of angles in an n sided shape. 
N will be greater than 2.
"""


def angle(n):
    return 180 * (n - 2)


def main():
    # Output: 180
    # n = 3
    # print(angle(n))

    assert angle(3) == 180
    assert angle(4) == 360


if __name__ == '__main__':
    main()

    