from collections.abc import MutableSequence, Sequence


def merge_sequence(a: MutableSequence, b: MutableSequence) -> MutableSequence:
    """Merging 'a' and 'b' in one sequence."""
    result = []
    while len(a) != 0 and len(b) != 0:
        el = a.pop(0) if a[0] < b[0] else b.pop(0)
        result.append(el)

    result += list(b) + list(a)
    return result


def merge(a: Sequence, b: Sequence) -> Sequence:
    """Merging 'a' and 'b' in one sequence."""
    result = []
    n, m = len(a), len(b)
    i, j = 0, 0

    while i != n and j != m:
        if a[i] < b[j]:
            el = a[i]
            i += 1
        else:
            el = b[j]
            j += 1

        result.append(el)

    result += a[i:] + b[j:]
    return result
