# Fast power

## Problem

Raise an integer base to a signed integer exponent. Python also supports a nonzero modulus. C provides iterative and recursive functions returning `double`.

## Idea

Read the binary digits of the exponent. Square the current factor for each successive bit and multiply it into the result only when the bit is set.

```text
result = 1; factor = base; remaining = abs(exponent)
while remaining > 0:
    if remaining is odd: result *= factor
    remaining = floor(remaining / 2)
    if remaining > 0: factor *= factor
return result
```

## Correctness

The product of `result` and `factor` raised to `remaining` stays equal to the original power. An odd bit moves one factor into the result. Squaring the factor and halving the remaining exponent preserves the rest. The same invariant holds modulo a nonzero modulus. A negative ordinary exponent uses a reciprocal. A negative modular exponent first finds the modular inverse.

## Complexity

- **Time.** O(log |e|) multiplications for nonzero exponent `e`. The bit cost of a Python multiplication depends on operand size, and a negative modular exponent also pays for inversion.
- **Space.** O(1) numeric variables for the loop. C recursion uses O(log |e|) stack frames. Python integers can grow with the size of the result.
- **Count.** The loop for nonzero `e` performs `bit_length(|e|) − 1` squarings and `popcount(|e|)` multiplications into the result. The recursive C variant has the same number of squarings and one fewer multiplication into the result.

Python uses the modulo convention of `pow`. C accepts the full signed exponent range and has the usual `double` rounding, overflow and underflow behavior.

## Implementations

- Python · [source](python/fast_power.py) · [tests](python/test_fast_power.py)
- C · [source](c/src/fastpow.c) · [header](c/include/fastpow.h) · [tests](c/tests/test_fast_power.c)
