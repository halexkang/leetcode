# https://leetcode.com/problems/two-sum/
# 1. Two Sum

# Idea:
# - given a num, we need to know if (target - num) was seen before
# - map (target - num) to num
def twoSum(nums, target):
    d = {}
    for i in range(len(nums)):
        if target - nums[i] in d: # (target - num) = compl
            return [d[target - nums[i]], i]
        d[nums[i]] = i
    return []