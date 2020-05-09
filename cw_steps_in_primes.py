"""Codewars: Steps in Primes
6 kyu

URL:https://www.codewars.com/kata/5613d06cee1e7da6d5000055/train/python

The prime numbers are not regularly spaced. For example from 
2 to 3 the step is 1. From 3 to 5 the step is 2. From 7 to 11 it is 4. 
Between 2 and 50 we have the following pairs of 2-steps primes:
3, 5 - 5, 7, - 11, 13, - 17, 19, - 29, 31, - 41, 43

We will write a function step with parameters:
g (integer >= 2) which indicates the step we are looking for,
m (integer >= 2) which gives the start of the search (m inclusive),
n (integer >= m) which gives the end of the search (n inclusive)

In the example above step(2, 2, 50) will return [3, 5] which is the 
first pair between 2 and 50 with a 2-steps.
So this function should return the first pair of the two prime numbers 
spaced with a step of g between the limits m, n if these g-steps prime 
numbers exist otherwise nil or null or None or Nothing or [] or "0, 0" 
or {0, 0} or 0 0(depending on the language).

#Examples:
step(2, 5, 7) --> [5, 7] or (5, 7) or {5, 7} or "5 7"
step(2, 5, 5) --> nil or ... or [] in Ocaml or {0, 0} in C++
step(4, 130, 200) --> [163, 167] or (163, 167) or {163, 167}
See more examples for your language in "RUN"

Remarks:
([193, 197] is also such a 2-steps primes between 130 and 200 but it's 
not the first pair).
step(6, 100, 110) --> [101, 107] though there is a prime between 101 
and 107 which is 103; the pair 101-103 is a 2-step.

#Notes: The idea of "step" is close to that of "gap" but it is not 
exactly the same. For those interested they can have a look at 
http://mathworld.wolfram.com/PrimeGaps.html.

A "gap" is more restrictive: there must be no primes in between 
(101-107 is a "step" but not a "gap" Next kata will be about "gaps":-).
For Go: nil slice is expected when there are no step between m and n. Example: step(2,4900,4919) --> nil
"""


def _is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def step(g, m, n):
    # Edge cases.
    if n - m < g:
        return None

    i = m
    while i + g <= n:
        # Two prime candidates: i, i+g
        if _is_prime(i) and _is_prime(i + g):
            return [i, i + g]
        else:
            i += 1

    return None


def _is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def step(g, m, n):
    # Edge cases.
    if n - m < g:
        return None

    # Create a dict:num->True or False for checking if prime.
    num_isprime_d = dict()

    i = m
    while i + g <= n:
        # Two prime candidates: i, i+g
        if i in num_isprime_d and (i + g) not in num_isprime_d:
            num_isprime_d[i + g] = _is_prime(i + g)
        elif i not in num_isprime_d and (i + g) not in num_isprime_d:
            num_isprime_d[i] = _is_prime(i)
            num_isprime_d[i + g] = _is_prime(i + g)

        if num_isprime_d[i] and num_isprime_d[i + g]:
            return [i, i + g]
        
        i += 1

    return None

# ----------------------------------------------------------------

def step(g, m, n): # run out of time
    if m == n:
        return None

    primes = []
    result = []

    while m <= n:
        # for i in range(2, m // 2 + 1):
        for i in range(2, int(m ** 0.5) + 1):
            if m % i == 0:
                break
        if m % i != 0:
            primes.append(m)
        m += 1
    
    length = len(primes)
    for i in range(length):
        if primes[i] and primes[i] + g in primes:
            result.append(primes[i])
            result.append(primes[i] + g)
            return result


def main():
    import time
    # # Output: [101, 103]
    # g, m, n = 2,100,110
    # print(step(g, m, n))

    runs = 50
    start_time = time.time()
    for _ in range(runs):
        assert step(2,100,100000) == [101, 103]
        assert step(4,100,100000) == [103, 107]
        # assert step(2,100,110) == [101, 103]
        # assert step(4,100,110) == [103, 107]
        # assert step(2,5,5) == None
        # assert step(6,100,110) == [101, 107]
        # assert step(8,300,400) == [359, 367]
        # assert step(10,300,400) == [307, 317]
    print('Time:', (time.time() - start_time) / runs)


if __name__ == '__main__':
    main()

