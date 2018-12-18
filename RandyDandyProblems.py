from collections import Counter

def factorialBottomUp(n):

    d = [1] * (n + 1)

    for i in range(1, n + 1):
        d[i] = d[i - 1] * i
    return d[n]

def swap(arr, i, j):
    temp = arr[i]
    arr[i], arr[j] = arr[j], temp

def minimumBribes(q):
    n = len(q)
    num_bribes = 0
    bribes = [0] * n
    i = 0
    while i < n - 1:
        if q[i] > q[i + 1]:
            bribes[q[i] - 1] += 1
            num_bribes += 1
            swap(q, i, i + 1)
            if bribes[q[i + 1] - 1] > 2:
                print('Too chaotic')
                return
            if i > 0:
                i -= 1
        else:
            i += 1
        # print(q)
        # print(bribes)
    print(num_bribes)

def twoStrings(s1, s2):
    """
    Given two strings s1 and s2, determine if they share a common substring
    Note that a substring could be just one character
    Solution:
    Given that even one character will suffice as a common substring, clearly
    any substring that contains more than one common character in sequence will
    share a common character
    """
    #brute force solution O(len(s1) * len(s2))
    # for c1 in s1:
    #     for c2 in s2:
    #         if c1 == c2:
    #             return 'YES'
    # return 'NO'

    # set solution O(len(s1)) since 'in' keyword is O(1) time
    all_chars = dict.fromkeys(set(s2), 1)
    for c in s1:
        if c in all_chars.keys():
            return 'YES'
    return 'NO'

def sherlockAndAnagrams(s):
    """
    two strings are anagrams of each other if the letters of one string
    can be rearranged to form the other string. Given a string, find the
    number of pair of substrings of the string that are anagrams of each other
    Ex. s = mom => angrammatic pairs : [m, m], [mo, om]
    """
    
    substrings = {}
    count = 0
    n = len(s)
    for i in range(1, n + 1):
        for j in range(i):
            sub = ''.join(sorted(s[j : i]))
            if sub in substrings:
                substrings[sub] += 1
            else:
                substrings[sub] = 0
            count += substrings[sub]
    return count

def getWays(n, c):
    """
    How many ways can you make change for a particular value n using
    m coins of distinct denomination.
    Ex. n = 10, c = [2, 5, 3, 6]
    => 5 ways : {2, 2, 2, 2, 2}, {2, 2, 3, 3}, {2, 2, 6}, {2, 3, 5}, {5, 5}
    Solution:
    # num ways to make change for n units with m coins = 
    # num ways to make change for n units not using the ith coin + 
    # num ways to make change for n units using the ith coin
    The recursive solution has too many overlapping function calls, so 
    we use DP to make it more efficient
    """
    d = {}

    return getWays(n, c[:-1], d) + getWays(n - c[-1], c, d)