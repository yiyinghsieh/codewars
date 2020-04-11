"""Irreducible Sum of Rationals
6 kyu

URL:https://www.codewars.com/kata/5517fcb0236c8826940003c9/train/python

You will have a list of rationals in the form
lst = [ [numer_1, denom_1] , ... , [numer_n, denom_n] ]
or
lst = [ (numer_1, denom_1) , ... , (numer_n, denom_n) ]
where all numbers are positive integers. You have to produce their 
sum N / D in an irreducible form: this means that N and D have only 1 
as a common divisor.

Return the result in the form:
[N, D] in Ruby, Crystal, Python, Clojure, JS, CS, PHP, Julia
Just "N D" in Haskell, PureScript
"[N, D]" in Java, CSharp, TS, Scala, PowerShell, Kotlin
"N/D" in Go, Nim
{N, D} in C++, Elixir
"{N, D}" in C
Some((N, D)) in Rust
Some "N D" in F#, Ocaml
c(N, D) in R
(N, D) in Swift
'(N D) in Racket

If the result is an integer (D evenly divides N) return:
an integer in Ruby, Crystal, Elixir, Clojure, Python, JS,CS,PHP,R,Julia
Just "n" (Haskell, PureScript)
"n" Java, CSharp, TS, Scala, PowerShell, Go, Nim, Kotlin
{n, 1} in C++
"{n, 1}" in C
Some((n, 1)) in Rust
Some "n" in F#, Ocaml,
(n, 1) in Swift
n in Racket

If the input list is empty, return
nil/None/null/Nothing
{0, 1} in C++
"{0, 1}" in C
"0" in Scala, PowerShell, Go, Nim
O in Racket
"" in Kotlin

Example:
[ [1, 2], [1, 3], [1, 4] ]  -->  [13, 12]

    1/2  +  1/3  +  1/4     =      13/12
Note
See sample tests for more examples and the form of results.
"""


def sum_fracts(lst):
    from fractions import Fraction

    if not lst:
        return None

    sum_i = 0
    for i in lst:
        sum_i += Fraction(i[0], i[1])
    if sum_i.numerator % sum_i.denominator == 0:
        return sum_i
    else:
        num_den = sum_i.numerator, sum_i.denominator
        return list(num_den)


def main():
    # # Output:[13, 12]
    # lst = [[1, 2], [1, 3], [1, 4]]
    # print(sum_fracts(lst))
    # # Output: 2
    # lst = [[1, 3], [5, 3]]
    # print(sum_fracts(lst))
    # # Output: None
    # lst = []
    # print(sum_fracts(lst))

    assert sum_fracts([[1, 2], [1, 3], [1, 4]]) == [13, 12]
    assert sum_fracts([[1, 3], [5, 3]]) == 2


if __name__ == '__main__':
    main()

