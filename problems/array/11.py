# https://leetcode.com/problems/container-with-most-water/description/
# 11. Container With Most Water

# Idea:
# - the only way to increase volume, is to move the limiting bar
#   because we are reducing width, height must increase
def maxArea(height):
    s, e = 0, len(height)-1
    max_vol = 0
    while s < e:
        if height[s] < height[e]: # if limiting factor is start
            curr_vol = height[s] * (e - s)
            s += 1
        else: # if limiting factor is end
            curr_vol = height[e] * (e - s)
            e -= 1
        max_vol = max(max_vol, curr_vol)
    return max_vol