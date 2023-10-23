# https://leetcode.com/problems/valid-anagram/description/
# 242. Valid Anagram

# Idea:
# - track frequency, check if frequency is the same for two strings
# - create two dictoinary and check if they are same

def isAnagram(s, t):
    ds = {}
    dt = {}
    for ch in s:
        if ch in ds:
            ds[ch] += 1
        else:
            ds[ch] = 1
    for ch in t:
        if ch in dt:
            dt[ch] += 1
        else:
            dt[ch] = 1
    return ds == dt