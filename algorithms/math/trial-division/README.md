# Trial division

## Problem

Determine exactly whether an integer is prime. The C implementation accepts a `uint64_t`. The Python implementation also accepts negative integers and returns false for values below two.

## Idea

Handle two and three directly. After eliminating their multiples, test potential divisors of the form `6k − 1` and `6k + 1`.

```text
if n <= 3: return n >= 2
if n is divisible by 2 or 3: return false
for i = 5, 11, 17, ... while i <= floor(sqrt(n)):
    if n is divisible by i or i + 2: return false
return true
```

## Correctness

A composite integer has a prime divisor at most √n. Any prime divisor greater than three is congruent to 1 or −1 modulo six, so the loop covers it. The C guard `i <= n / i` avoids squaring near the integer limit. Python computes the square root exactly with integer arithmetic.

## Complexity

- **Time.** O(√n) divisibility checks in the worst case. This counts arithmetic operations. For Python integers, division also depends on the number of bits.
- **Space.** O(1) machine words in C and a fixed number of potentially large integers in Python.
- **Count.** After the checks for two and three, each visited pair tests at most two remainders.

## Implementations

- Python · [source](python/is_prime.py) · [tests](python/test_trial_division.py)
- C · [source](c/src/isprime.c) · [header](c/include/isprime.h) · [tests](c/tests/test_trial_division.c)
