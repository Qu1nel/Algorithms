# Shaker sort

## Problem

Sort a sequence with alternating adjacent passes. Equal keys keep their input order.

## Idea

Bubble a minimum to the left on the backward pass, then a maximum to the right on the forward pass. Shrink the active range from both ends.

```text
copy the input into a list
left = 0; right = n - 1
while left < right:
    walk backward from right, swapping inverted adjacent pairs
    if there were no swaps: stop
    walk forward from left, swapping inverted adjacent pairs
    left += 1; right -= 1
return the copy
```

## Correctness

After the backward scan a minimum of the active range is at `left`. The forward scan leaves it in place and moves a maximum to `right`. Both fixed ends can be skipped. A backward pass with no swaps already establishes that the active range has ordered adjacent pairs.

## Complexity

- **Time.** Θ(n) in the best case and Θ(n²) in the worst case.
- **Space.** Θ(n) for the returned list and Θ(1) extra working space.
- **Count.** A full backward-and-forward round over `w` active items does `2(w − 1)` comparisons. Sorted input stops after `n − 1` comparisons for `n ≥ 1`.

## Implementations

- Python · [source](python/shaker_sort.py) · [tests](python/test_shaker_sort.py)
