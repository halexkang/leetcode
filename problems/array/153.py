# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
# 153. Find Minimum in Rotated Sorted Array

# Idea:
# - if O(n), look for not increasing number -> solution
# - this problem can be reduced to finding a first true value in a true false array
# - [false, false ... true, true true ...], condition = val < nums[0]
# - right -> mid, left -> mid+1 
def findMin(nums):
    l, r = 0, len(nums)-1
    if nums[r] > nums[l]: # if not rotated
        return nums[l]
    while l < r:
        mid = (l + r)//2
        if nums[mid] >= nums[0]: # false cond
            l = mid + 1
        else:
            r = mid
    return nums[l]