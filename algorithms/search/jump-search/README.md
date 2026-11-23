# Jump search

## Problem

Find a target in a nondecreasing sequence with constant-time indexing. Return an index of the target or −1. With duplicates, use the rightmost match in the first block whose endpoints bracket the target.

## Idea

Use a jump length of ⌊√n⌋. Probe the endpoints of overlapping blocks, then run binary search inside the first candidate block.

```text
if items is empty: return -1
step = integer_square_root(length(items))
for left = 0, step, 2 * step, ... below length(items):
    right = min(length(items) - 1, left + step)
    if items[left] <= target <= items[right]:
        return rightmost binary search within [left, right]
return -1
```

## Correctness

Every index is covered by a block. Sorted order rules out all blocks whose endpoint values fail to bracket the target. If a candidate brackets the target strictly, any occurrence is inside that block. If an endpoint equals the target, that endpoint already provides a match. Binary search gives the rightmost match within the selected block.

## Complexity

- **Time.** O(⌈n/s⌉ + log(s + 1)) for jump length `s`, so O(√n) with this choice of `s`.
- **Auxiliary space.** Θ(1).
- **Count.** At most ⌈n/s⌉ block probes, at most two key comparisons per probe, followed by at most ⌈log₂(s + 1)⌉ midpoint comparisons and one final equality.

## Implementations

- Python · [source](python/jump_search.py) · [tests](python/test_jump_search.py)
