# https://leetcode.com/problems/longest-consecutive-sequence/
# 128. Longest Consecutive Sequence

# Idea:
# - we are looking for consecutive numbers -> does n+1 exists, n-1 exists
# - use a set to look for it
# - if we find a prev_num or post_num, continue to look for consecutive
# - removing the element from set after finding it will make time complexity O(n)

def longestConsecutive(nums):
    s = set(nums)
    max_len = 0
    for num in nums:
        cnt = 1 # starts at 1 since length is never 0
        prev_num = num - 1
        while prev_num in s: # look left, if found continue looking
            cnt += 1
            s.remove(prev_num)
            prev_num -= 1
        post_num = num + 1
        while post_num in s: # look right, if found continue looking
            cnt += 1
            s.remove(post_num)
            post_num += 1
        max_len = max(max_len, cnt) # update max length
    return max_len