"""Codewars: Are they the "same"?
6 kyu

URL:https://www.codewars.com/kata/550498447451fbbd7600041c/train/python

Given two arrays a and b write a function comp(a, b)
(compSame(a, b) in Clojure) that checks whether the two arrays have
the "same" elements, with the same multiplicities. "Same" means,
here, that the elements in b are the elements in a squared,
regardless of the order.

Examples
Valid arrays
a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a, b) returns true because in b 121 is the square of 11, 14641 is 
the square of 121, 20736 the square of 144, 361 the square of 19, 25921
the square of 161, and so on. It gets obvious if we write b's elements
in terms of squares:

a = [121, 144, 19, 161, 19, 144, 19, 11] 
b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
Invalid arrays
If we change the first number to something else, comp may not return 
true anymore:

a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a,b) returns false because in b 132 is not the square of any 
number of a.

a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
comp(a,b) returns false because in b 36100 is not the square of any 
number of a.

Remarks
a or b might be [] (all languages except R, Shell). a or b might be nil
or null or None or nothing (except in Haskell, Elixir, C++, Rust, R,
Shell, PureScript).

If a or b are nil (or null or None), the problem doesn't make sense so 
return false.

If a or b are empty then the result is self-evident.

a or b are empty or not empty lists.
"""


def comp(a1, a2):
    from collections import defaultdict

    # Edge cases.
    if a1 is None or a2 is None:
        return False

    # Create dict:a1->count & dict:a2->count.
    a1_squared_count_d = defaultdict(int)
    for i in a1:
        a1_squared_count_d[i ** 2] += 1

    a2_count_d = defaultdict(int)
    for i in a2:
        a2_count_d[i] += 1

    # Iterate through a2 numbers to check its existence and count match.
    for i, count in a2_count_d.items():
        if i not in a1_squared_count_d or a1_squared_count_d[i] != count:
            return False
            
    return True 


def comp1(a1, a2):
    try:
        return sorted([i ** 2 for i in a1]) == sorted(a2)
    except:
        return False


def comp2(a1, a2):
    return None not in (a1,a2) and [i*i for i in sorted(a1)]==sorted(a2)


def main():
    # Output: True
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    print(comp(a1,a2))
   
    # # Output: False
    a1 = [58, 42, 0, 0, 70, 38, 97]
    a2 = [3364, 1764, 0, 1, 4900, 1444, 9409]
    print(comp1(a1,a2))

    # # Output: False
    a1 = [12, 45, 1, 36, 5, 36]
    a2 = [144, 2025, 1, 1296, 25, 1297]
    print(comp2(a1,a2))


    # a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    # a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    # assert comp(a1, a2) == True
    
    # a1 = [83, 72, 82, 3, 48, 42] 
    # a2 = [6889, 5184, 6724, 9, 2304, 1764]
    # assert comp(a1, a2) == True
    
    # a1 = [91, 13, 2, 12, 91, 44, 53] 
    # a2 = [8281, 169, 4, 144, 8281, 1936, 2809]
    # assert comp(a1, a2) == True
    
    # a1 = [7] 
    # a2 = [49]
    # assert comp(a1, a2) == True
    
    # a1 = [35] 
    # a2 = [1226]
    # assert comp(a1, a2) == False
    
    # a1 = [90, 22, 92] 
    # a2 = [8100, 484, 8464]
    # assert comp(a1, a2) == True

    # a1 = [58, 42, 0, 0, 70, 38, 97]
    # a2 = [3364, 1764, 0, 1, 4900, 1444, 9409]
    # assert comp(a1, a2) == False

    # a1 = [12, 45, 1, 36, 5, 36]
    # a2 = [144, 2025, 1, 1296, 25, 1297]
    # assert comp(a1, a2) == False

    # a1 = [] 
    # a2 = [8100, 484, 8464]
    # assert comp(a1, a2) == False

    # a1 = [90, 22, 92] 
    # a2 = []
    # assert comp(a1, a2) == False

    # a1 = [] 
    # a2 = []
    # assert comp(a1, a2) == True


if __name__ == '__main__':
    main()



