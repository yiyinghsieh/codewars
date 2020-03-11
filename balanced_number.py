"""Balanced Number (Special Numbers Series #1 )
7 kyu

URL: https://www.codewars.com/kata/5a4e3782880385ba68000018/train/python

Definition
Balanced number is the number that * The sum of all digits to the left 
of the middle digit(s) and the sum of all digits to the right of the 
middle digit(s) are equal*.

Task
Given a number, Find if it is Balanced or not .

Warm-up (Highly recommended)
Playing With Numbers Series
Notes
If the number has an odd number of digits then there is only one middle
digit, e.g. 92645 has middle digit 6; otherwise, there are two middle 
digits , e.g. 1301 has middle digits 3 and 0

The middle digit(s) should not be considered when determining whether 
a number is balanced or not, e.g 413023 is a balanced number because 
the left sum and right sum are both 5.

Number passed is always Positive .
Return the result as String

Input >> Output Examples
(balanced-num 7) ==> return "Balanced"
Explanation:
Since , The sum of all digits to the left of the middle digit (0)
and the sum of all digits to the right of the middle digit (0) are 
equal , then It's Balanced

(balanced-num 295591) ==> return "Not Balanced"
Explanation:
Since , The sum of all digits to the left of the middle digits (11)
and the sum of all digits to the right of the middle digits (10) are 
Not equal , then It's Not Balanced
Note : The middle digit(s) are 55 .

(balanced-num 959) ==> return "Balanced"
Explanation:
Since , The sum of all digits to the left of the middle digits (9)
and the sum of all digits to the right of the middle digits (9) are 
equal , then It's Balanced
Note : The middle digit is 5 .

(balanced-num 27102983) ==> return "Not Balanced"
Explanation:
Since , The sum of all digits to the left of the middle digits (10)
and the sum of all digits to the right of the middle digits (20) are 
Not equal , then It's Not Balanced
Note : The middle digit(s) are 02 .
"""


def balanced_num(number):
    num_len = len(str(number))
    if num_len == 1 or num_len == 2:
        return "Balanced"
    elif num_len % 2 == 0:
        each_len = int((num_len - 2) / 2)  #int
        sum_right = sum([int(i) for i in str(number)[:each_len]])
        sum_left = sum([int(i) for i in str(number)[-each_len:]])
        if sum_right == sum_left:
            return "Balanced"
        else:
            return "Not Balanced"
    else:
        each_len = int((num_len - 1) / 2) #int
        sum_right = sum([int(i) for i in str(number)[:each_len]])
        sum_left = sum([int(i) for i in str(number)[-each_len:]])
        if sum_right == sum_left:
            return "Balanced"
        else:
            return "Not Balanced"

    
def main():
    # # Output: "Balanced"
    # number = 959
    # print(balanced_num(number))

    # # Output: "Not Balanced"
    # number = 1230987
    # print(balanced_num(number))

    # # Output: "Balanced"
    # number = 56239814
    # print(balanced_num(number))

    assert balanced_num(7) == "Balanced"
    assert balanced_num(959) == "Balanced"
    assert balanced_num(13) == "Balanced"
    assert balanced_num(432) == "Not Balanced"
    assert balanced_num(424) == "Balanced"

    assert balanced_num(1024) == "Not Balanced"
    assert balanced_num(66545) == "Not Balanced"
    assert balanced_num(295591) == "Not Balanced"
    assert balanced_num(1230987) == "Not Balanced"
    assert balanced_num(56239814) == "Balanced"


if __name__ == '__main__': 
    main()

