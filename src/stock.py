from typing import List


def maxProfit(prices: List[int]) -> int:
    buy = prices[0]
    sell = None
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] - buy > profit:
            sell = prices[i]
            profit = sell - buy
        if prices[i] < buy:
            buy = prices[i]

    return profit


# prices = [7, 1, 5, 3, 6, 4]
# prices = [7, 6, 4, 3, 1]
prices = [7, 1, 4, 3, 7, 0, 5]
print(maxProfit(prices))
