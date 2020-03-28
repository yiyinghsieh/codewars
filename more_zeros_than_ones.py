"""More Zeros than Ones
6 kyu

URL:https://www.codewars.com/kata/5d41e16d8bad42002208fe1a/train/python

Create a moreZeros function which will receive a string for input, and 
return an array containing only the characters from that string whose 
binary representation of its ASCII value consists of more zeros than 
ones.

You should remove any duplicate characters, keeping the first 
occurence of any such duplicates, so they are in the same order in the
final array as they first appeared in the input string.

Examples
'abcde' === ["1100001", "1100010", "1100011", "1100100", "1100101"]
               True       True       False      True       False

        --> ['a','b','d']

'DIGEST'--> ['D','I','E','T']

All input will be valid strings of length > 0. Leading zeros in binary 
should not be counted.
"""
def _new_s(s):
    s_lst = []
    length = len(s)
    for i in range(length):
        if s[i] not in s_lst:
            s_lst.append(s[i])
    return s_lst


def _ascii_value(s):
    s_ascii_value = []
    for x in _new_s(s):
        ascii_value = ord(x)
        s_ascii_value.append(ascii_value)
    return s_ascii_value

        
def _binary(s):
    binary_lst = []
    for i in _ascii_value(s):
        binary = bin(i)[2:]
        binary_lst.append(binary)
    return binary_lst


def _count_1_0_True_False(s):
    lst = []
    binary_s = _binary(s)
    length = len(binary_s)
    num = 0
    while num < length:
        count_1 = 0
        count_0 = 0
        for i in binary_s[num]: 
            if int(i) == 1:
                count_1 += 1
            else:
                count_0 += 1
        if count_1 < count_0:
            lst.append('True')
        else:
            lst.append('False')
        num += 1
    return lst


def more_zeros(s):
    lst = _count_1_0_True_False(s)
    length = len(lst)
    result = []
    for i in range(length):
        if lst[i] == 'True':
            new_s = _new_s(s)[i]
            result.append(new_s)
    return result


def main():
    # # Output: ['a', 'b', 'd']
    # s = 'abbcde'
    # s = 'thequickbrownfoxjumpsoverthelazydog'
    # print(_new_s(s))
    # print(_ascii_value(s))
    # print(_binary(s))
    # print(_count_1_0_True_False(s))
    # print(more_zeros(s))

    assert more_zeros('abcde') == ['a', 'b', 'd']
    assert more_zeros('thequickbrownfoxjumpsoverthelazydog') == ['h', 'b', 'p', 'a', 'd']
    assert more_zeros('THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG') == ['T', 'H', 'E', 'Q', 'I', 'C', 'B', 'R', 'F', 'X', 'J', 'P', 'L', 'A', 'D']
    assert more_zeros('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_') == ['a', 'b', 'd', 'h', 'p', 'A', 'B', 'C', 'D', 'E', 'F', 'H', 'I', 'J', 'L', 'P', 'Q', 'R', 'T', 'X', '0']
    assert more_zeros('DIGEST') == ['D', 'I', 'E', 'T']

    # assert more_zeros2('abcde') == ['a', 'b', 'd']
    # assert more_zeros2('thequickbrownfoxjumpsoverthelazydog') == ['h', 'b', 'p', 'a', 'd']
    # assert more_zeros2('THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG') == ['T', 'H', 'E', 'Q', 'I', 'C', 'B', 'R', 'F', 'X', 'J', 'P', 'L', 'A', 'D']
    # assert more_zeros2('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_') == ['a', 'b', 'd', 'h', 'p', 'A', 'B', 'C', 'D', 'E', 'F', 'H', 'I', 'J', 'L', 'P', 'Q', 'R', 'T', 'X', '0']
    # assert more_zeros2('DIGEST') == ['D', 'I', 'E', 'T']


if __name__ == '__main__':
    main()

