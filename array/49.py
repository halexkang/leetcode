# https://leetcode.com/problems/group-anagrams/description/
# 49. Group Anagrams

# Idea:
# - can use sort, but counting sort scales better O(N*logN) vs O(N)
from collections import defaultdict

def groupAnagrams(strs):
    d = defaultdict(list)
    for s in strs:
        cnts = [0]*26
        for ch in s:
            cnts[ord(ch) - ord('a')] += 1
        d[tuple(cnts)].append(s)
    return d.values()