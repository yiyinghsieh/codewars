"""Codewars: Remove duplicate words
7 kyu

URL: https://www.codewars.com/kata/5b39e3772ae7545f650000fc/train/python

Your task is to remove all duplicate words from a string, leaving only 
single (first) words entries.

Example:
Input:
'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma 
delta'
Output:
'alpha beta gamma delta'
"""


def remove_duplicate_words(s):
    word_count_d = dict()
    words = s.split()
    lst = []
    for word in words:
        word_count_d[word] = word_count_d.get(word, 0) + 1
        if word_count_d[word] == 1:
            lst.append(word)
    return ' '.join(lst)



def remove_duplicate_words(s):
    words = s.split()
    dedup_words = []
    for w in words:
        if w not in dedup_words:
            dedup_words.append(w)
    return ' '.join(dedup_words)


# The order of output is wrong
# def remove_duplicate_words(s):
#     word_count_d = dict()
#     words = s.split()
#     for word in words:
#         word_count_d[word] = word_count_d.get(word, 0) + 1
#     return ' '.join(word_count_d.keys())


# def remove_duplicate_words(s):
#     words = s.split()
#     return ' '.join(set(words))


def main():
    # Output: 'alpha beta gamma delta'
    s = 'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'
    print(remove_duplicate_words(s))


if __name__ == '__main__':
    main()



