# Find single element in a sorted array
def binary_search(arr, target):
    left, right = 1, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1


# Find first index satisfying a condition
# Finding the first index satisfying a condition is the same as finding the first true value of a true-false array.
# ex: [False, ... False, True, ... True]
def condition():
    pass

def binary_search(arr):
    left, right = 1, len(arr)-1
    while left < right:
        mid = (left + right) // 2
        if condition():
            right = mid
        else:
            left = mid + 1
    return left