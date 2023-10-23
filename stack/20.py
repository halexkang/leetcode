# https://leetcode.com/problems/valid-parentheses/description/
# 20. Valid Parentheses

# Idea:
# - if we see opening, push closing to the stack
# - if we see closing, pop from stack and check match

# Fail cases:
# 1) more opening than closing
# 2) more closing than opening
# 2) not matching parenthesis
def isValid(s):
    opened = ['[', '(', '{']
    closed = [']', ')', '}']
    stack = []
    for ch in s:
        if ch in opened: # if opening
            stack.append(ch)
        else: # if closing
            if not len(stack): # if stack is tempty, fail case 1
                return False
            if stack[-1] != opened[closed.index(ch)]: # if doesnt' match, fail case 3
                return False
            stack.pop()
    return len(stack) == 0 # make sure stack is empty, fail case 2