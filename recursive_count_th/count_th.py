"""
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurrences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
"""
"""
Polya

1)	Understand the problem
What is out input?
The input is string

What are the restrictions?
The restriction is that we need to find the occurrences of "th" word within a string we are passing
The function must be recursive, no loops are allowed

What does our function return?
function should return a count of how many occurrences of "th" occur within word. Case matters

2) Plan

"""


def count_th(word, target="th"):
    n1 = len(word)
    n2 = len(target)

    if n1 == 0 or n1 < n2:
        return 0

    if word[0:n2] == target:
        return count_th(word[n2:], target) + 1

    return count_th(word[n2 - 1:], target)
