# Quicksort

## Problem

Return a sorted list using randomized three-way partitioning. Equal keys keep their input order.

## Idea

Choose a random pivot and distribute the input into smaller, equal and greater partitions in input order. Use an explicit work stack to visit partitions in sorted order.

```text
push the input as pending work
while work remains:
    take the top entry
    if it is ready or contains at most one element: append it
    else:
        choose a uniform pivot from the entry
        partition it into smaller, equal and greater keys
        push greater work, the ready equal run, then smaller work
```

## Correctness

All keys of the lower partition precede all keys of the equal run, which precedes the upper partition. Each unfinished child is smaller than its parent. The stack emits the lower partition first and stores each partition in input order, so ties remain stable.

## Complexity

- **Time.** Θ(n) when all keys are equal, O(n log n) in expectation over uniform pivots, and Θ(n²) in the worst case.
- **Space.** O(n) additional memory for the work stack, partitions and returned list. Pending partitions hold disjoint sets of elements.
- **Count.** A partition of length `m ≥ 2` makes between `m` and `2m` key comparisons. The explicit work stack handles repeated extreme pivots within Python's ordinary call-stack limit.

## Implementations

- Python · [source](python/quick_sort.py) · [tests](python/test_quick_sort.py)
