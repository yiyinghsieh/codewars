"""Codewars: Well of Ideas - Easy Version
8 kyu

URL: https://www.codewars.com/kata/well-of-ideas-easy-version/train/python

For every good kata idea there seem to be quite a few bad ones!

In this kata you need to check the provided array (x) for good ideas 'good' 
and bad ideas 'bad'. If there are one or two good ideas, return 'Publish!', 
if there are more than 2 return 'I smell a series!'. If there are no good ideas, 
as is often the case, return 'Fail!'.

test.describe("Static Cases")
test.assert_equals(well(['bad', 'bad', 'bad']), 'Fail!')
test.assert_equals(well(['good', 'bad', 'bad', 'bad', 'bad']), 'Publish!')
test.assert_equals(well(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 
'bad', 'good']), 'I smell a series!')
"""


from __future__ import division
from __future__ import print_function


def well(x):

    count_good = 0
   
    for word in x:
        if word == 'good':
            count_good += 1
    
    if count_good == 0:
        return 'Fail!'
    elif count_good == 1 or count_good == 2:
        return 'Publish!'
    elif count_good > 2:
        return 'I smell a series!'


def well1(x):
    word = x.count('good')

    if word == 0:
        return 'Fail!'
    elif word > 2:
        return 'I smell a series!'
    else:
        return 'Publish!'

def main():
    # Output:'Fail!'
    x = ['bad', 'bad', 'bad']
    print(well(x))

    # Output:'Publish!'
    x = ['good', 'bad', 'bad', 'bad', 'bad']
    print(well(x))

    # Output:'I smell a series!'
    x = ['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']
    print(well(x))


if __name__ == '__main__':
    main()




