"""
Given an array of nums with length n, find all elements
a, b, c in nums such that a + b + c = 0
(note solution set cannot contain duplicates triplets)
"""
from itertools import combinations

def three_sum(nums):

    tups = []
    nums.sort()
    l = 0
    r = len(nums)
    d = {}
    for i, val in enumerate(nums):
        if val in d:
            d[val].append(i)
        else:
            d[val] = [i]
    while l < r:
        a = nums[l]
        for i in range(l + 1, len(nums)):
            b = nums[i]
            c = -(a + b)
            if c in d:
                for j in range(len(d[c])):
                    if i + 1 <= d[c][j] < r:
                        tups.append((a, b, c))
                        j = len(d[c])
                    
        l += 1
    return list(set(tups))

if __name__ == '__main__':

    nums = [-1, 0, 1, 2, -1, -4]
    print(three_sum(nums))
