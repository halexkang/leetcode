# https://leetcode.com/problems/valid-palindrome/submissions/
# 125. Valid Palindrome

# Idea:
# - two pointers from each end
# - can be optimized by not preprocessing string, 
#   and ignoring/lowercasing on the fly

def isPalindrome(s):
    lst = []
    # remove non alphanum, make everything lowercase
    for ch in s:
        if ch.isalnum():
            lst.append(ch.lower())
    new_s = ''.join(lst)
    start, end = 0, len(new_s)-1
    res = True
    while start < end:
        if new_s[start] != new_s[end]:
            res = False
            break
        start += 1
        end -= 1
    return res