/*
 * Fast power by repeated squaring.
 *
 * [Time-Complexity]: O(log |n|) multiplications for nonzero n
 * [Space-Complexity]: O(1) iterative; O(log |n|) recursive
 */

#include "fastpow.h"

#include <stdio.h>

static uint64_t exponent_magnitude(int64_t n)
{
    /* Adding one before negation keeps INT64_MIN representable. */
    return n < 0 ? (uint64_t)(-(n + 1)) + 1 : (uint64_t)n;
}

static double power_base(int64_t a, int64_t n)
{
    if (a == 0 && n < 0) {
        fprintf(stderr, "Zero cannot be raised to a negative exponent.\n");
        exit(EXIT_FAILURE);
    }
    return n < 0 ? 1.0 / (double)a : (double)a;
}

static double power_recursive(double base, uint64_t n)
{
    if (n == 0) return 1.0;
    if (n == 1) return base;

    double half = power_recursive(base, n / 2);
    double square = half * half;
    return n % 2 == 0 ? square : base * square;
}

double fast_power_r(int64_t a, int64_t n)
{
    return power_recursive(power_base(a, n), exponent_magnitude(n));
}

double fast_power_c(int64_t a, int64_t n)
{
    double result = 1.0;
    double base = power_base(a, n);
    uint64_t remaining = exponent_magnitude(n);

    while (remaining != 0) {
        if (remaining % 2 != 0) result *= base;
        remaining /= 2;
        if (remaining != 0) base *= base;
    }
    return result;
}
