# https://leetcode.com/problems/product-of-array-except-self/submissions/
# 238. Product of Array Except Self

# Idea:
# - product of array except self is equivalent to (product before number * product after number)
# - prepopulate a pre arr and post arr

def productExceptSelf(nums):
    pre = [1] * len(nums)
    post = [1] * len(nums)
    for i in range(1, len(nums)): # pre arr
        pre[i] = pre[i-1] * nums[i-1]
        post[-1-i] = post[-1-i+1] * nums[-1-i+1]
    for i in range(len(nums)-2, -1, -1): # post arr
        post[i] = post[i+1] * nums[i+1]
    for i in range(len(nums)):
        nums[i] = pre[i] * post[i]
    return nums