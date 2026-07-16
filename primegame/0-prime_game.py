#!/usr/bin/python3
"""Prime Game module."""


def isWinner(x, nums):
    """Determine who wins the most rounds of the Prime Game.

    Args:
        x (int): number of rounds.
        nums (list): list of n values, one per round.

    Returns:
        str: name of the player with the most wins ("Maria" or "Ben"),
        or None if the winner cannot be determined.
    """
    if x is None or nums is None or x < 1 or len(nums) < 1:
        return None

    n = max(nums)
    if n < 2:
        sieve = []
    else:
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if sieve[i]:
                for multiple in range(i * i, n + 1, i):
                    sieve[multiple] = False

    prime_count = [0] * (n + 1)
    count = 0
    for i in range(2, n + 1):
        if sieve[i]:
            count += 1
        prime_count[i] = count

    maria_wins = 0
    ben_wins = 0

    for round_n in nums:
        if round_n < 2:
            ben_wins += 1
        elif prime_count[round_n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None