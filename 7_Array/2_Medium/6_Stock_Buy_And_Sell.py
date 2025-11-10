'''
Problem Statement: You are given an array of prices where prices[i] is the price of a given stock on an ith day.
'''
# Method - 1
def maxprofit(prices):
    max_profit = 0
    n = len(prices)

    for i in range(n):
        for j in range(i + 1, n):
            profit = prices[j] - prices[i]  # sell after buying
            if profit > max_profit:
                max_profit = profit

    return max_profit

# Method - 2
def maxprofit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit


prices = [7,1,5,3,6,4]
print(maxprofit(prices))
