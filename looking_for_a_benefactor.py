"""Looking for a benefactor

7 kyu

URL: https://www.codewars.com/kata/569b5cec755dd3534d00000f/train/python

The accounts of the "Fat to Fit Club (FFC)" association are supervised by 
John as a volunteered accountant. The association is funded through 
financial donations from generous benefactors. John has a list of the 
first n donations: [14, 30, 5, 7, 9, 11, 15] He wants to know how much the 
next benefactor should give to the association so that the average of the 
first n + 1 donations should reach an average of 30. After doing the math 
he found 149. He thinks that he made a mistake. Could you help him?

if dons = [14, 30, 5, 7, 9, 11, 15] then new_avg(dons, 30) --> 149

The function new_avg(arr, navg) should return the expected donation 
(rounded up to the next integer) that will permit to reach the average 
navg.
Should the last donation be a non positive number (<= 0) John wants us to 
throw (or raise) an error or
. return Nothing in Haskell
. return None in F#, Ocaml, Scala
. return -1 in C, Fortran, Nim, PowerShell, Go, Prolog
. echo ERROR in Shell
. raise-argument-error in Racket
so that he clearly sees that his expectations are not great enough.

Notes:
. all donations and navg are numbers (integers or floats), arr can be empty.
. See examples below and "Test Samples" to see which return is to be done.
new_avg(    , 92) should return 645
new_avg([14, 30, 5, 7, 9, 11, 15], 2) 
should raise an error (ValueError or invalid_argument or argument-error or 
DomainError) 
or return `-1` or ERROR or Nothing or None depending on the language
"""


def new_avg(arr, newavg):
    import math

    # Edge case for arr = [].
    if not arr:
        return newavg

    n = len(arr)
    total = sum(arr)
    exp_total = (n + 1) * newavg

    if exp_total <= total:
        raise ValueError('Last donation is a non positive number (<= 0)')
    else:
        exp_donate = exp_total - total
        return math.ceil(exp_donate)


def main():
    # Output: 628
    arr = [14, 30, 5, 7, 9, 11, 16]
    newavg = 90
    print(new_avg(arr, newavg))

    # Output: 645
    arr = [14, 30, 5, 7, 9, 11, 15]
    newavg = 92
    print(new_avg(arr, newavg))

    # Output: None 
    arr = [14, 30, 5, 7, 9, 11, 15]
    newavg = 2
    print(new_avg(arr, newavg))


if __name__ == '__main__':
    main()

