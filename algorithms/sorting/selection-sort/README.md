# Selection sort

## Problem

Return a sorted list of the items in a sequence.

## Idea

Find the smallest remaining key in the unsorted suffix and move it to the next position of the sorted prefix.

```text
copy the input into a list
for i from 0 to n - 2:
    minimum = index of a smallest item in items[i..n)
    if minimum != i: swap items[i] and items[minimum]
return the copy
```

## Correctness

After `i` passes, the prefix of length `i` contains the `i` smallest items in order. Finding the minimum of the remaining suffix and placing it at index `i` extends the invariant. A long-distance swap can change the relative order of equal keys.

## Complexity

- **Time.** Θ(n²) comparisons for every input order.
- **Space.** Θ(n) for the returned list and Θ(1) extra working space.
- **Count.** The scans perform `(n − 1) + (n − 2) + … + 1 = n(n − 1)/2` comparisons. At most `n − 1` swaps are needed for `n ≥ 1`.

## Implementations

- Python · [source](python/selection_sort.py) · [tests](python/test_selection_sort.py)
