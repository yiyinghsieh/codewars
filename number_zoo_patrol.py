"""Number Zoo Patrol
6 kyu

URL:https://www.codewars.com/kata/5276c18121e20900c0000235/train/python

Background:
You're working in a number zoo, and it seems that one of the numbers has 
gone missing!

Zoo workers have no idea what number is missing, and are too incompetent 
to figure it out, so they're hiring you to do it for them.

In case the zoo loses another number, they want your program to work 
regardless of how many numbers there are in total.

Task:
Write a function that takes a shuffled list of unique numbers from 1 to 
n with one element missing (which can be any number including n). 
Return this missing number.

Note: huge lists will be tested.

Examples:
[1, 3, 4]  =>  2
[1, 2, 3]  =>  4
[4, 2, 3]  =>  1
"""


def find_missing_number(numbers):



def main():
	# Output: 1
	numbers = [2, 3, 4]
	print(find_missing_number(numbers))


# Test.assert_equals(find_missing_number([2, 3, 4]), 1)
# Test.assert_equals(find_missing_number([1, 3, 4]), 2)
# Test.assert_equals(find_missing_number([1, 2, 4]), 3)
# Test.assert_equals(find_missing_number([1, 2, 3]), 4)



if __name__ == '__main__':
	main()











