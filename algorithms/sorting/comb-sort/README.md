# Comb sort

## Problem

Return a sorted list of the items in a sequence.

## Idea

Compare at a gap that shrinks from the list length by a factor of about 1.247. Large gaps can move keys a long way early. Finish with adjacent comparisons.

```text
copy the input into a list
gap = n; swapped = false
while gap > 1 or swapped:
    gap = max(1, floor(gap * 1000 / 1247))
    swapped = false
    for i from 0 to n - gap - 1:
        if items[i] > items[i + gap]: swap them; swapped = true
return the copy
```

## Correctness

All operations are swaps, so the input elements are preserved. The integer gap strictly decreases to one. The subsequent passes are bubble passes. Once a gap-one pass makes no swaps, every adjacent pair is ordered.

## Complexity

- **Time.** Θ(n log n) in the best case because the geometric gap schedule still runs. Gap-one cleanup gives an O(n²) worst-case bound.
- **Space.** Θ(n) for the returned list and Θ(1) extra working space.
- **Count.** A pass at gap `g` makes `n − g` comparisons.

## Implementations

- Python · [source](python/comb_sort.py) · [tests](python/test_comb_sort.py)
