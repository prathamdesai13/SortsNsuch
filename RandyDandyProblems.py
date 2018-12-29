from collections import Counter
from DataStructs.MinHeap import MinHeap
from Algos.sorts import mergesort
from operator import itemgetter

def factorialBottomUp(n):

    d = [1] * (n + 1)

    for i in range(1, n + 1):
        d[i] = d[i - 1] * i
    return d[n]

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

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

def matchingStrings(strings, queries):
    freq = Counter(strings)
    print(freq)
    count = [0] * len(queries)
    for i, q in enumerate(queries):
        if q in freq.keys():
            count[i] += freq[q]
    return count

def minMaxRiddle(arr):
    """
    Given an integer array of size n, find the maximum of the minimums of 
    every window size in the array, with window sizes ranging from 1 to n.
    Ex. arr = [6, 3, 5, 1, 12], n = len(arr) = 5
    Window size 1: (6), (3), (5), (1), (12) => max = 12
    Window size 2: (6, 3), (3, 5), (5, 1), (1, 12) => max = 3
    Window size 3: (6, 3, 5), (3, 5, 1), (5, 1, 12) => max = 3
    Window size 4: (6, 3, 5, 1), (3, 5, 1, 12) => max = 1
    Window size 5: (6, 3, 5, 1, 12) => max = 1
    """
    # the most brutal brute force can get, i think cubic time:
    # n = len(arr)
    # window_maxs = []
    # for w in range(1, n + 1):
    #     window_max = 0
    #     for i in range(n - w + 1):
    #         window = arr[i : i + w]
    #         window_min = min(window)
    #         if window_min > window_max:
    #             window_max = window_min
    #     window_maxs.append(window_max)
    # return window_maxs

    # little better, quyadratic time
    n = len(arr)
    mins = [[0 for _ in range(n)] for _ in range(n)]
    mins[0] = arr
    maxes = [max(mins[0])]
    for i in range(1, n):
        curr_max = 0
        for j in range(n - i):
            mins[i][j] = min(mins[i - 1][j], mins[i - 1][j + 1])
            if mins[i][j] > curr_max:
                curr_max = mins[i][j]
        maxes.append(curr_max)
    return maxes
def pairs(k, arr):
    """
    return number of pairs of numbers in integer array arr
    that have a difference of k
    """
    # brute force solution:
    # pairs = 0
    # n = len(arr)
    # for i in range(n):
    #     for j in range(i + 1, n):
    #         if abs(arr[i] - arr[j]) == k:
    #             pairs += 1
    # return pairs
    
    # efficient solution:

    pairs = 0
    arr = mergesort(arr)

    j = 0
    i = 1
    while i < len(arr):
        diff = arr[i] - arr[j]

        if diff > k:
            j += 1
        elif diff == k:
            i += 1
            pairs += 1
        else:
            i += 1
    return pairs

def luck_balance(k, contests):
    # some hackerrank problem on luck (greedy i think)
    # contests is a list of integer tuples and k is some int
    # using min heap, quadratic time:
    # total_luck = 0
    # k_heap = MinHeap()
    # for pair in contests:
    #     if pair[1] == 1:
    #         k_heap.insert(pair[0])
    # k_heap.heapify()
    # while len(k_heap.tree) - 1 > k:
    #     k_heap.delete_min()
    # for pair in contests:
    #     if pair[1] == 0:
    #         total_luck += pair[0]
    #     else:
    #         if pair[0] in k_heap.tree:
    #             total_luck += pair[0]
    #         else:
    #             total_luck -= pair[0]
    # return total_luck
    
    # using itemgetter, nlogn + n time
    total_luck = 0
    contests = sorted(contests, key=itemgetter(0))
    for pair in reversed(contests):
        luck, importance = pair
        if importance == 0:
            total_luck += luck
        else:
            if k > 0:
                total_luck += luck
                k -= 1
            else:
                total_luck -= luck
    return total_luck

def minimum_swaps(arr):
    """
    Given an unordered array of size n with elements in 
    [1, 2, ..., n] with no duplicates, return the minimum
    number of swaps required to go from the unordered array
    to an ordered array.
    Ex. [7, 1, 3, 2, 4, 5, 6]
    => Swap (0, 3) : [2, 1, 3, 7, 4, 5, 6]
    => Swap (0, 1) : [1, 2, 3, 7, 4, 5, 6]
    => Swap (3, 4) : [1, 2, 3, 4, 7, 5, 6]
    => Swap (4, 5) : [1, 2, 3, 4, 5, 7, 6]
    => Swap (5, 6) : [1, 2, 3, 4, 5, 6, 7]
    5 total swaps took place to order the array
    """
    # linear time, fastest solution i think
    i = 0
    n = len(arr)
    num_swaps = 0
    while i < n:
        x = arr[i]
        og_index = x - 1
        if i != og_index:
            swap(arr, i, og_index)
            print("Swap:({}, {})".format(i, og_index))
            num_swaps += 1
        else:
            i += 1
    return num_swaps

def makeAnagrams(s1, s2):
    """
    Given two strings, not necessarilly of equal length,
    find minimum number of chars deleted from the strings
    to make them anagrams.
    Ex. s1 = 'cde', s2 = 'abc' => 4 removals : {'d', 'e', 'a', 'b'}
    """
    # f1 = dict(Counter(s1))
    # f2 = dict(Counter(s2))
    # all_chars = set(list(f1.keys()) + list(f2.keys()))
    # count = 0
    # for c in all_chars:
    #     if c in f1 and c not in f2:
    #         count += f1[c]
    #     elif c not in f1 and c in f2:
    #         count += f2[c]
    #     else:
    #         if f1[c] != f2[c]:
    #             count += abs(f1[c] - f2[c])
    # return count

    # another sol:
    all_chars = [0] * 26
    for c in s1:
        all_chars[ord(c) - ord('a')] += 1
    
    for c in s2:
        all_chars[ord(c) - ord('a')] -= 1

    count = 0
    for i in range(26):
        count += abs(all_chars[i])

    return count

def alternatingCharacters(s):
    """
    Given a string containing only A's and B's, find
    minimum number of deletions of characters in the string
    such that the final string has no matching adjacent chars.
    Ex. AABAAB -> ABAAB -> ABAB => 2 deletions
    """
    i = 0
    count = 0
    while i < len(s):
        j = i + 1
        c = s[i]
        mini_count = 0
        while j < len(s) and s[j] == c:
            j += 1
            mini_count += 1
        count += mini_count
        s = s[:i + 1] + s[j:]
        i = j - mini_count
    return count