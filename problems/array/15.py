# https://leetcode.com/problems/3sum/description/
# 15. 3Sum

# Clarification: 
# - can use same numbers, just can't use the same index
# - even if diff index, answer can't contain duplicates

# Idea:
# - 1. if 3 0s exist, we can use (0, 0, 0)
# - 2. if 0 exists, we can use (0, -num, num)
# - for sum of a pair, check if -sum exists
#   - 3. (neg + neg) = -pos
#   - 4. (pos + pos) = -neg

def threeSum(nums):
    p, n = [], [] # need to be list to contain duplicates
    z = 0
    for num in nums:
        if num == 0:
            z += 1
        if num > 0:
            p.append(num)
        if num < 0:
            n.append(num)
    p_set = set(p) # keep a set for constant lookup
    n_set = set(n) # keep a set for constant lookup
    res = set() # even if different index, it should not contain duplicates
    if z >= 3: # case 1
        res.add(tuple([0, 0, 0]))
    if z >= 1: # case 2
        for num in p:
            if -num in n_set:
                res.add(tuple(sorted([num, 0, -num])))
    for i in range(len(n)): # case 3
        for j in range(i+1, len(n)): # i+1 because we don't want (i,j) * (j,i)
            if i == j:
                continue
            if -(n[i]+n[j]) in p_set:
                res.add(tuple(sorted([n[i], n[j], -(n[i]+n[j])])))
    for i in range(len(p)): # case 4
        for j in range(i+1, len(p)): # i+1 because we don't want (i,j) * (j,i)
            if i == j:
                continue
            if -(p[i]+p[j]) in n_set:
                res.add(tuple(sorted([p[i], p[j], -(p[i]+p[j])])))
    return res