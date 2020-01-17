"""Codewars: Count the divisors of a number
7 kyu

URL: https://www.codewars.com/kata/542c0f198e077084c0000c2e

Count the number of divisors of a positive integer n.
Random tests go up to n = 500000.

Examples
divisors(4)  = 3  # 1, 2, 4
divisors(5)  = 2  # 1, 5
divisors(12) = 6  # 1, 2, 3, 4, 6, 12
divisors(30) = 8  # 1, 2, 3, 5, 6, 10, 15, 30
"""


def divisors1(n): # 8
    lst = []
    nums = list(range(1, n + 1))
    for num in nums:
        if n % num == 0:
            lst.append(num)
    return len(lst)


def divisors11(n): # 4
    lst = []
    nums = list(range(1, n//2 + 1))
    for num in nums:
        if n % num == 0:
            lst.append(num)
    return len(lst) + 1

def divisors12(n): # 3
    counter = 0
    nums = list(range(1, n//2 + 1))
    for num in nums:
        if n % num == 0:
            counter += 1
    return counter + 1


def divisors2(n): # 5
    nums = range(1, n + 1)
    return len([num for num in nums if n % num == 0])


def divisors3(n): # 7
    return len([num for num in range(1, n + 1) if n % num == 0])


def divisors4(n): # 6
    return sum(1 for num in range(1, n + 1) if n % num == 0)


def divisors5(n): # 9
    return sum(n%num==0 for num in range(1, n + 1))


def divisors6(n): # 1
    counter = 0
    for num in range(1, n//2 + 1):
        if n % num == 0:
            counter += 1
    return counter + 1


def divisors7(n): # 2
    return len([num for num in range(1, n//2 + 1) if n % num == 0]) + 1
    # range n <not include n>
    # +1 <add n>


def main():
    import time

    # Output = 13
    n = 4096
    # print(divisors(n))

    start_time = time.time()
    print('divisors1 time', divisors1(n), time.time()-start_time)

    start_time = time.time()
    print('divisors11 time', divisors11(n), time.time()-start_time)

    start_time = time.time()
    print('divisors12 time', divisors12(n), time.time()-start_time)

    start_time = time.time()
    print('divisors2 time', divisors2(n), time.time()-start_time)

    start_time = time.time()
    print('divisors3 time', divisors3(n), time.time()-start_time)

    start_time = time.time()
    print('divisors4 time', divisors4(n), time.time()-start_time)

    start_time = time.time()
    print('divisors5 time', divisors5(n), time.time()-start_time)

    start_time = time.time()
    print('divisors6 time', divisors6(n), time.time()-start_time)

    start_time = time.time()
    print('divisors7 time', divisors7(n), time.time()-start_time)

    # assert divisors(4) == 3
    # assert divisors(5) == 2
    # assert divisors(12) == 6
    # assert divisors(30) == 8
    # assert divisors(4096) == 13


if __name__ == '__main__':
    main()

