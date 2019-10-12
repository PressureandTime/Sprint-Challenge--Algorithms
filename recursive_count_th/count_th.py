"""
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
"""

"""
Polya

1)	Understand the problem
What is out input?
The input is string

What are the restrictions?
The restriction is that we need to find the occurences of "th" word within a string we are passing
The function must be recursive, no loops are allowed

What does our function return?
function should return a count of how many occurences of "th" occur within word. Case matters

2) Plan

"""


def count_th(word, target="th"):

    n1 = len(word)
    n2 = len(target)

    if n1 == 0 or n1 < n2:
        return 0

    if word[0:n2] == target:
        return count_th(word[n2 - 1 :], target) + 1

    return count_th(word[n2 - 1 :], target)


####********* CODE BELOW I AM KEEPING FOR FUTURE REFERENCE AND PRACTICE

# print(count_th("basdthe"))


# str = "basdthe"

# str2 = str[0:2]

# print(str2)


# niz = "basdth"

# niz2 = niz[1:]

# print(niz2)


# proba = 'he'

# proba2 = proba[0:1]

# print(len(proba2))


# numbers = [0, 1, 2, 3, 4, 5]

# string = "the"

# string2 = string[0:2]
# numbers2 = numbers[0:2]

# print(string2)
