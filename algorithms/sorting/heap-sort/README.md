# Heap sort

## Problem

Return a sorted list of the items in a sequence using a max-heap.

## Idea

Build a heap from the bottom up. Move its maximum to the end of the active prefix, then restore the heap with iterative sift-down.

```text
copy the input into a list
for each internal node from bottom to top:
    sift down within the full list
for end from n - 1 down to 1:
    swap items[0] and items[end]
    sift down within items[0..end)
return the copy
```

## Correctness

Sift-down swaps a node with its larger child until it dominates both children. Building from the bottom ensures the children already root valid heaps. The root is a maximum, so each extraction puts the next maximum at the beginning of the sorted suffix. Moving the root can change the order of equal keys.

## Complexity

- **Time.** Heap construction takes O(n) by summing the heights of internal nodes. The worst-case total is Θ(n log n). With all keys equal, each sift stops at the root and the total is Θ(n).
- **Space.** Θ(n) for the returned list and Θ(1) extra working space.
- **Count.** Each sift compares the children and compares the node with the larger child at most once per level.

## Implementations

- Python · [source](python/heap_sort.py) · [tests](python/test_heap_sort.py)
