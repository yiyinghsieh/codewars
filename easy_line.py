"""Easy Line
7 kyu

URL: https://www.codewars.com/kata/56e7d40129035aed6c000632/train/python

In the drawing below we have a part of the Pascal's triangle, lines are 
numbered from zero (top).

[     [1],
     [1, 1],
    [1, 2, 1],
  [1, 3, 3, 1],
 [1, 4, 6, 4, 1],
 ...
]

We want to calculate the sum of the squares of the binomial coefficients 
on a given line with a function called easyline (or easyLine or easy-line).
Can you write a program which calculate easyline(n) where n is the line 
number?
The function will take n (with: n>= 0) as parameter and will return the 
sum of the squares of the binomial coefficients on line n.

##Examples:
easyline(0) => 1
easyline(1) => 2
easyline(4) => 70
easyline(50) => 100891344545564193334812497256

##Ref: http://mathworld.wolfram.com/BinomialCoefficient.html
"""


def easyline1(n):
    if n <= 1:
        return sum([1] * (n + 1))
    
    # Create "raw" Pascal's triangle
    T = []
    for i in range(n + 1):
        T.append([1] * (i + 1)) 
    
    # Iterate through rows to update middle numbers.
    for i in range(2, n + 1):
        for j in range(1, len(T[i]) - 2 + 1):
            T[i][j] = T[i-1][j-1] + T[i-1][j]
    
    # Take the last to compute sum of squares.
    squared_sum = 0
    for num in T[-1]:
        squared_sum += num**2
    return squared_sum


def easyline2(n):
    if n <= 1:
        return sum([1] * (n + 1))

    T = []
    for i in range(n + 1):
        T.append([1] * (i + 1))

        for j in range(1, len(T[i]) - 2 + 1):
            T[i][j] = T[i - 1][j - 1] + T[i - 1][j]

    squared_sum = 0
    for num in T[-1]:
        squared_sum += num **2
    return squared_sum


def main():
    # Output: 1
    n = 0
    print(easyline1(n))
    print(easyline2(n))

    # Output: 2
    n = 1
    print(easyline1(n))
    print(easyline2(n))

    # Output: 6
    n = 2
    print(easyline1(n))
    print(easyline2(n))

    # Output: 20
    n = 3
    print(easyline1(n))
    print(easyline2(n))

    # Output: 70
    n = 4
    print(easyline1(n))
    print(easyline2(n))

    # Output: 252
    n = 5
    print(easyline1(n))
    print(easyline2(n))


if __name__ == '__main__':
    main()

