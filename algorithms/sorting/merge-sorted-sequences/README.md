# Merge sorted sequences

## Problem

Return a sorted list combining two nondecreasing sequences `a` and `b`. When two leading keys compare equal, take the element from `b` first.

## Idea

Keep one index per sequence and append the smaller current element. Once a sequence is exhausted, append the other suffix.

```text
i = j = 0
while both sequences have unread items:
    append the smaller leading item; take from b on a tie
    advance the corresponding index
append the unread suffix
return the result
```

## Correctness

The smallest unconsumed key is at one of the two current indices. Appending it extends the sorted output and preserves the order of items within each source. Once either source is exhausted, the other suffix is already ordered.

## Complexity

- **Time.** Θ(n + m) for `merge` with constant-time indexing. The `merge_sequence` variant removes consumed prefixes by popping from the front. For lists, those shifts can cost O((n + m)²).
- **Space.** Θ(n + m) for the returned list and Θ(1) extra working space.
- **Count.** At most `n + m − 1` key comparisons when both inputs are nonempty. `merge_sequence` expects two separate mutable inputs and leaves the unconsumed suffix in its source.

## Implementations

- Python · [source](python/merge.py) · [tests](python/test_merge.py)
