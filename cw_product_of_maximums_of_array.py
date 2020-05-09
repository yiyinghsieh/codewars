"""Codewars: Product Of Maximums Of Array (Array Series #2)
7 kyu

URL: https://www.codewars.com/kata/5a63948acadebff56f000018/train/python

Task
Given an array/list [] of integers , Find the product of the k maximal numbers.

Notes
Array/list size is at least 3 .
Array/list's numbers Will be mixture of positives , negatives and zeros
Repetition of numbers in the array/list could occur.

Input >> Output Examples
maxProduct ({4, 3, 5}, 2) ==>  return (20)
Explanation:
Since the size (k) equal 2 , then the subsequence of size 2 whose gives product 
of maxima is 5 * 4 = 20 .
maxProduct ({8, 10 , 9, 7}, 3) ==>  return (720)
Explanation:
Since the size (k) equal 3 , then the subsequence of size 2 whose gives product 
of maxima is 8 * 9 * 10 = 720 .
maxProduct ({10, 8, 3, 2, 1, 4, 10}, 5) ==> return 
"""


def max_product(lst, n_largest_elements):
    lst = sorted(lst, reverse = True)
    maximal = 1
    for i in lst[0 : n_largest_elements]:
        maximal *= i
    return maximal

def main():
    # Output: 720
    # lst = [10,8,7,9]
    # n_largest_elements = 3
    # print(max_product(lst, n_largest_elements))

    # Test.it("Basic Tests")
    assert max_product([0]*10, 5) == 0
    assert max_product([4,3,5], 2) == 20
    assert max_product([10,8,7,9], 3) == 720
    assert max_product([8,6,4,6], 3) == 288
    # Test.it("Larger arrays")   
    assert max_product(list(range(10, -1, -1)), 5) == 10*9*8*7*6
    assert max_product([10,2,3,8,1,10,4], 5), 9600
    assert max_product([13,12,-27,-302,25,37,133,155,-1], 5) == 247895375
    # Test.it("Arrays with negative values")
    assert max_product([-4,-27,-15,-6,-1],2) == 4
    assert max_product([-17,-8,-102,-309],2) == 136
    # Test.it("Arrays with positive and negative values")
    assert max_product([10,3,-27,-1], 3) == -30
    assert max_product([14,29,-28,39,-16,-48],4) == -253344

if __name__ == '__main__':
    main()

