# Merge sort

## Problem

Return a sorted list of the items in a sequence. Preserve the relative order of equal keys.

## Idea

Split a list in half, sort each half recursively, then merge the two sorted halves with left-first tie handling.

```text
sort(items):
    if length(items) <= 1: return items
    left, right = split items into two halves
    return merge(sort(left), sort(right), take from left on ties)
```

## Correctness

The empty and singleton cases are sorted. Given two correctly sorted halves, merging places the smallest remaining item next. Choosing from the left on ties retains the order of equal keys across the split. Induction on the length establishes correctness.

## Complexity

- **Time.** Θ(n log n) for growing inputs. Each level copies and merges Θ(n) elements and there are Θ(log n) levels.
- **Space.** O(n) peak additional memory, including slices and result. The recursion depth is O(log n).
- **Count.** For `n` a positive power of two, the worst-case comparison count is `n log₂ n − n + 1`.

## Implementations

- Python · [source](python/merge_sort.py) · [tests](python/test_merge_sort.py)
