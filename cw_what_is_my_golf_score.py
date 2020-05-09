"""Codewars: What is my golf score?
7 kyu

URL: https://www.codewars.com/kata/59f7a0a77eb74bf96b00006a/train/python

I have the par value for each hole on a golf course and my stroke score 
on each hole. I have them stored as strings, because I wrote them down 
on a sheet of paper. Right now, I'm using those strings to calculate my 
golf score by hand: take the difference between my actual score and the 
par of the hole, and add up the results for all 18 holes.

For example:
If I took 7 shots on a hole where the par was 5, my score would be: 
7 - 5 = 2
If I got a hole-in-one where the par was 4, my score would be: 
1 - 4 = -3.
Doing all this math by hand is really hard! Can you help make my life 
easier?
Task Overview
Complete the function which accepts two strings and calculates the golf 
score of a game. Both strings will be of length 18, and each character 
in the string will be a number between 1 and 9 inclusive.
"""


def golf_score_calculator(par_string, score_string):
    ar_sum = 0
    score_sum = 0    
    for par in par_string:
        par_sum += int(par)
    for score in score_string:
        score_sum += int(score)
    return score_sum - par_sum


def golf_score_calculator(par_string, score_string):
    par_sum = sum([int(par) for par in par_string])
    score_sum = sum([int(score) for score in score_string])
    return score_sum - par_sum


def golf_score_calculator(par_string, score_string):
    return sum([int(score) - int(par) for par, score in zip(par_string, score_string)])


def main():
    # Output: -1
    par_string = '443454444344544443'
    score_string = '353445334534445344'
    print(golf_score_calculator(par_string, score_string))


if __name__ == '__main__':
    main()

