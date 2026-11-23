#ifndef MATH_FAST_POWER_H
#define MATH_FAST_POWER_H

#include <inttypes.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

/*
 * Return a to the signed exponent n as a double.
 * The recursive version uses O(log |n|) multiplications and stack frames.
 * Zero raised to a negative exponent reports an error and exits.
 */
extern double fast_power_r(int64_t a, int64_t n);


/*
 * Return a to the signed exponent n using O(1) auxiliary space.
 * The domain and error behavior match fast_power_r.
 */
extern double fast_power_c(int64_t a, int64_t n);

#endif  // MATH_FAST_POWER_H
