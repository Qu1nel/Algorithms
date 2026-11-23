#ifndef MATH_FAST_POWER_H
#define MATH_FAST_POWER_H

#include <inttypes.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

/*
 * A recursive implementation of a fast algorithm for computing the degree b of a number a.
 *
 * Time O(log(n)).
 * Memory O(n)
 *
 */
extern double fast_power_r(int64_t a, int64_t n);


/*
 * Realization of the algorithm of fast degree expansion on the basis of a loop to calculate the degree b of a number a.
 *
 * Time O(log(n)).
 * Memory O(n)
 *
 */
extern double fast_power_c(int64_t a, int64_t n);

#endif  // MATH_FAST_POWER_H
