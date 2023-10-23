# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# 121. Best Time to Buy and Sell Stock

# Idea:
# - we want to find a min and a max, but the max has to come after min
# - if profit is negative, then a new min has been found (update curr min -> new min)
# - if profit is positive, keep looking for new max from curr min
def maxProfit(prices):
    s, e = 0, 1
    max_profit = 0
    while e < len(prices):
        curr_max = prices[e] - prices[s]
        max_profit = max(max_profit, curr_max)
        if curr_max < 0:
            s = e
        else:
            e += 1
    return max_profit