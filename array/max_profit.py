"""
Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""


def max_profit_bf(prices):
    """
    O(n^2)
    """
    profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            tmp = prices[j] - prices[i]
            if tmp > profit:
                profit = tmp
    return profit


def max_profit_optim(prices):
    profit = 0
    buy = prices[0]
    for sell in prices[1:]:
        if sell > buy:
            profit = max(profit, sell - buy)
        else:
            buy = sell
    return profit


if __name__ == "__main__":
    prices = [7, 6, 4, 3, 1]
    print(max_profit_optim(prices))
