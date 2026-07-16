# Prime Game

Interview-prep project (Holberton School) covering an algorithmic game
theory problem.

## Task 0. Prime Game

Maria and Ben play `x` rounds of a game. Each round starts with the set
of consecutive integers `1..n`. Players alternate turns (Maria first),
each turn picking a prime number still present in the set and removing
it along with all of its multiples. The player who cannot pick a prime
loses that round.

`isWinner(x, nums)` returns the name of the player who won the most
rounds across `x` games (`nums` holding the `n` for each round), or
`None` if both players won an equal number of rounds.

### Approach

For a fixed `n`, the outcome only depends on the **parity of the count
of prime numbers ≤ n**:

- If that count is odd, Maria (first player) wins the round.
- If that count is even, Ben wins the round.

This holds because every legal move removes exactly one not-yet-used
prime (and its multiples, which are irrelevant to future prime
choices), so the total number of moves available in a round equals the
number of primes ≤ n, and the players simply alternate through them.

The implementation builds a Sieve of Eratosthenes up to
`max(nums)`, then a prefix-sum array of prime counts, so each round is
resolved in O(1) after an O(n log log n) precomputation.

### Usage

```
./main_0.py
```