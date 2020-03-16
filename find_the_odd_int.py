"""Find the odd int
7 kyu

URL: https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python

Given an array, find the integer that appears an odd number of times.

There will always be only one integer that appears an odd number of 
times.
"""


def find_it1(seq):
    # Create a dict:num->count.
    num_count_d = dict()
    for num in seq:
        num_count_d[num] = num_count_d.get(num, 0) + 1

    for k, v in num_count_d.items():
        if v % 2 != 0:
            return k
    
def find_it1(seq):
    from collections import defaultdict
    # Create a dict:num->count.
    num_count_d = defaultdict(int)  # default count = 0
    for num in seq:
        num_count_d[num] += 1

    for k, v in num_count_d.items():
        if v % 2 != 0:
            return k


def find_it2(seq):
    return [i for i in seq if seq.count(i) % 2][0] # only one odd num
    

def main():
    # Output: 5
    seq = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
    print(find_it1(seq))

    assert find_it1([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]) == 5
    assert find_it1([1,1,2,-2,5,2,4,4,-1,-2,5]) == -1
    assert find_it1([20,1,1,2,2,3,3,5,5,4,20,4,5]) == 5
    assert find_it1([10]) == 10
    assert find_it1([1,1,1,1,1,1,10,1,1,1,1]) == 10
    assert find_it1([5,4,3,2,1,5,4,3,2,10,10]) == 1

    assert find_it2([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]) == 5
    assert find_it2([1,1,2,-2,5,2,4,4,-1,-2,5]) == -1
    assert find_it2([20,1,1,2,2,3,3,5,5,4,20,4,5]) == 5
    assert find_it2([10]) == 10
    assert find_it2([1,1,1,1,1,1,10,1,1,1,1]) == 10
    assert find_it2([5,4,3,2,1,5,4,3,2,10,10]) == 1


if __name__ == '__main__':
    main()

