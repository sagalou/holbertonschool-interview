#!/usr/bin/python3
"""Module that makes change for an amount of money."""


def makeChange(coins, total):
    """Determine the fewest number of coins needed to meet total.

    Args:
        coins (list): list of coin denominations available.
        total (int): the amount to reach.

    Returns:
        int: fewest number of coins needed, or -1 if not possible.
             0 if total is 0 or less.
    """
    if total <= 0:
        return 0

    # dp[i] = fewest coins needed to make amount i
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount and dp[amount - coin] + 1 < dp[amount]:
                dp[amount] = dp[amount - coin] + 1

    return dp[total] if dp[total] != float('inf') else -1
