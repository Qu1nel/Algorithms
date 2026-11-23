# Bubble sort

## Problem

Return a sorted list of the items in a sequence. Equal keys keep their input order.

## Idea

Scan adjacent pairs from left to right and swap inverted pairs. Each pass moves the largest remaining item to the right end. Stop after a pass with no swaps.

```text
copy the input into a list
for end from n - 1 down to 1:
    swapped = false
    for i from 0 to end - 1:
        if items[i] > items[i + 1]: swap them; swapped = true
    if not swapped: stop
return the copy
```

## Correctness

After each pass the last item of the active range is a maximum, and the fixed suffix is in its final order. If a pass makes no swap, every adjacent pair in the active range is ordered. Strict comparisons leave equal keys in their original order.

## Complexity

- **Time.** Θ(n) in the best case and Θ(n²) in the worst case.
- **Space.** Θ(n) for the returned list and Θ(1) extra working space.
- **Count.** A sorted list of length `n ≥ 1` needs `n − 1` comparisons. A reverse-sorted list with distinct keys needs `n(n − 1)/2`. Each adjacent swap removes one inversion.

## Implementations

- Python · [source](python/bubble_sort.py) · [tests](python/test_bubble_sort.py)
