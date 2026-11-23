<p align="center">
  <img src=".github/assets/welcome.png" alt="Welcome" />
</p>

# Algorithms

[![Algorithms CI](https://github.com/Qu1nel/Algorithms/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/Qu1nel/Algorithms/actions/workflows/tests.yml?query=branch%3Amain)

A personal study notebook by [@Qu1nel](https://github.com/Qu1nel) for algorithms,
proofs, and complexity analysis. Each algorithm has a README with its problem,
pseudocode, correctness argument and cost model. Implementations and tests live
in language folders next to the explanation.

## Search

- [Binary search](algorithms/search/binary-search/README.md) · Python
- [Jump search](algorithms/search/jump-search/README.md) · Python

## Sorting

- [Bubble sort](algorithms/sorting/bubble-sort/README.md) · Python
- [Shaker sort](algorithms/sorting/shaker-sort/README.md) · Python
- [Selection sort](algorithms/sorting/selection-sort/README.md) · Python
- [Insertion sort](algorithms/sorting/insertion-sort/README.md) · Python
- [Comb sort](algorithms/sorting/comb-sort/README.md) · Python
- [Heap sort](algorithms/sorting/heap-sort/README.md) · Python
- [Merge sorted sequences](algorithms/sorting/merge-sorted-sequences/README.md) · Python
- [Merge sort](algorithms/sorting/merge-sort/README.md) · Python
- [Quicksort](algorithms/sorting/quick-sort/README.md) · Python

## Mathematics

- [Fast power](algorithms/math/fast-power/README.md) · Python and C
- [Trial division](algorithms/math/trial-division/README.md) · Python and C
- [Miller–Rabin primality test](algorithms/math/miller-rabin/README.md) · Python and C

## Run the checks

Use Python 3.11 or newer and GCC with C17 support. Set `CC` to the compiler
executable if you use another compiler.

```sh
python tests/run_checks.py
```

Each Python suite can also run on its own with `unittest`.

```sh
python -m unittest discover -s algorithms/search/binary-search/python
```

## License

[MIT](LICENSE) © [Ivan Kovach](https://github.com/Qu1nel)
