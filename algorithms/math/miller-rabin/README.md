# Miller–Rabin primality test

## Problem

Test an integer for primality with a positive number `k` of rounds. A passing result means probable prime. Python raises `ValueError` for a nonpositive round count; the C function returns false for zero rounds.

## Idea

For odd `n > 3`, write `n − 1 = 2ˢd` with odd `d`. A round checks powers of a random base starting at `aᵈ mod n`, then following the chain of squares.

```text
handle small integers and even candidates
write n - 1 = 2^s * d, with d odd
repeat k times:
    choose a uniformly from [2, n - 2]
    x = a^d mod n
    pass the round if x is 1 or n - 1
    otherwise square x modulo n up to s - 1 times
    pass if a square equals n - 1; reject if no pass occurs
return probable prime
```

## Correctness

For prime `n`, Fermat's theorem makes the final member of the squaring chain equal to one. In a field modulo a prime the only square roots of one are `1` and `−1`. Thus the chain starts at one or encounters minus one before reaching one. Rabin's theorem bounds the fraction of passing bases for each odd composite by one quarter. Independent uniform draws give a false-acceptance probability at most `4⁻ᵏ`. The implementations use general-purpose pseudorandom generators. [Rabin's original paper](https://doi.org/10.1016/0022-314X(80)90084-0)

## Complexity

- **Time.** O(k log n) modular multiplications. C uses overflow-safe repeated doubling, giving O(k log² n) modular additions as an upper bound. In a bit model, multiply the modular-multiplication count by the cost of the chosen arithmetic.
- **Space.** O(1) machine words for C and a fixed number of O(log n)-bit residues in Python.
- **Count.** After modular powering, a round uses at most `s − 1` more squarings and stops as soon as the result is known.

## Implementations

- Python · [source](python/is_prime.py) · [tests](python/test_miller_rabin.py)
- C · [source](c/src/isprime.c) · [header](c/include/isprime.h) · [tests](c/tests/test_miller_rabin.c)
