# Binary search

## Problem

Find the rightmost index of a target in a nondecreasing sequence. Return −1 when the target is absent. Indexing and comparison take constant time in the analysis.

## Idea

Halve an interval until it contains only one possible index. A midpoint that is at most the target becomes the new left endpoint, so equal items to its right can still be considered.

```text
if items is empty: return -1
left = 0; right = length(items)
while right - left > 1:
    mid = left + (right - left) // 2
    if items[mid] > target: right = mid
    else: left = mid
return left if items[left] == target else -1
```

## Correctness

If the target occurs, its rightmost index remains in `[left, right)`. A midpoint above the target eliminates it and everything after it. Otherwise, any occurrence before the midpoint cannot be the rightmost if `items[mid]` equals the target, and there is no occurrence before it if `items[mid]` is smaller. Each step shrinks the interval. The final equality checks the sole remaining index and also handles an absent target.

## Complexity

- **Time.** Θ(log n) for growing nonempty inputs and Θ(1) for empty or single-item inputs.
- **Auxiliary space.** Θ(1).
- **Count.** At most ⌈log₂ n⌉ midpoint comparisons and one final equality for `n > 0`. Empty input needs zero key comparisons. For `[1, 2, 2, 5]`, searching for `2` returns `2`.

## Implementations

- Python · [source](python/binary_search.py) · [tests](python/test_binary_search.py)
