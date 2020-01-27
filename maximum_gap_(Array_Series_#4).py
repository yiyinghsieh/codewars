"""Codewars: Maximum Gap (Array Series #4)
7 kyu

URL: https://www.codewars.com/kata/5a7893ef0025e9eb50000013/train/python

Task
Given an array/list [] of integers , Find The maximum difference between the 
successive elements in its sorted form.

Notes
Array/list size is at least 3 .
Array/list's numbers Will be mixture of positives and negatives also zeros_
Repetition of numbers in the array/list could occur.
The Maximum Gap is computed Regardless the sign.

Input >> Output Examples
maxGap ({13,10,5,2,9}) ==> return (4)
Explanation:
The Maximum Gap after sorting the array is 4, The difference between 9 - 5 = 4
maxGap ({-3,-27,-4,-2}) ==> return (23)
Explanation:
The Maximum Gap after sorting the array is 23, The difference between 
|-4- (-27) | = 23 .
Note : Regardless the sign of negativity .
maxGap ({-7,-42,-809,-14,-12}) ==> return (767)  
Explanation:
The Maximum Gap after sorting the array is 767, The difference between 
| -809- (-42) | = 767 .
Note : Regardless the sign of negativity .
maxGap ({-54,37,0,64,640,0,-15}) //return (576)
Explanation:
The Maximum Gap after sorting the array is 576 , The difference between 
| 64 - 640 | = 576 .
Note : Regardless the sign of negativity .
"""


def max_gap(numbers):
    gap_big = 0
    numbers_sort = sorted(numbers, reverse = True)
    i_last = numbers_sort[0]
    for i in numbers_sort:
        gap = i_last - i
        i_last = i
        if gap > gap_big:
            gap_big = gap
    return gap_big


def max_gap(numbers): 
    gap_big = 0 
    numbers.sort(reverse = True)
    for i in range(len(numbers) - 1):
        if numbers[i] - numbers[i + 1] > gap_big:
            gap_big = numbers[i] - numbers[i + 1]
    return gap_big


def main():
    # Output: 4
    # numbers = [13,10,2,9,5]
    # print(max_gap(numbers))
    # Test.describe("Basic tests")
    assert max_gap([13,10,2,9,5]) == 4
    assert max_gap([13,3,5]) == 8
    assert max_gap([24,299,131,14,26,25]) == 168
    assert max_gap([-3,-27,-4,-2]) == 23
    assert max_gap([-7,-42,-809,-14,-12]) == 767
    assert max_gap([12,-5,-7,0,290]) == 278
    assert max_gap([-54,37,0,64,-15,640,0]) == 576
    assert max_gap([130,30,50]) == 80
    assert max_gap([1,1,1]) == 0
    assert max_gap([-1,-1,-1]) == 0
    # print("<COMPLETEDIN::>")


if __name__ == '__main__':
    main()

