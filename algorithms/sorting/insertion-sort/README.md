# Insertion sort

## Problem

Return a sorted list by inserting each element into an already sorted prefix. The Python function retains the name `insert_sort`.

## Idea

Move each new item left through the prefix while it is strictly less than its predecessor.

```text
copy the input into a list
for i from 1 to n - 1:
    j = i
    while j > 0 and items[j] < items[j - 1]:
        swap items[j] and items[j - 1]
        j -= 1
return the copy
```

## Correctness

Before a pass, the prefix through index `i − 1` is sorted. Elements larger than the new item move right by one. The new item stops at the beginning or after an item no greater than itself. The extended prefix is sorted, and equal keys keep their original order.

## Complexity

- **Time.** Θ(n) in the best case and Θ(n²) in the worst case.
- **Space.** Θ(n) for the returned list and Θ(1) extra working space.
- **Count.** The number of swaps equals the number of inversions in the input. A reverse order of distinct keys takes `n(n − 1)/2` key comparisons.

## Implementations

- Python · [source](python/insertion_sort.py) · [tests](python/test_insertion_sort.py)
