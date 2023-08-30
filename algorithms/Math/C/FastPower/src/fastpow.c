/*
 * [Time-Complexity]: O()
 *
 * [Space-Complexity]: O()
 *
 */

#include "fastpow.h"

#include <stdio.h>

static double _fast_power_r(int64_t a, int64_t n)
{
    if (n == 1) return (double)a;
    if (n % 2 == 0) {
        return _fast_power_r(a * a, n / 2);
    } else {
        return (double)a * _fast_power_r(a * a, (n - 1) / 2);
    }
}

static double _fast_power_c(int64_t a, int64_t n)
{
    double result = 1;
    double mult = (double)a;

    while (n != 0) {
        if (n % 2 != 0) {
            result *= mult;
        }
        mult *= mult;
        n /= 2;
    }
    return result;
}

extern double fast_power_r(int64_t a, int64_t n)
{
    if (a == 0 && n < 0) {
        fprintf(stderr, "Math result not representable: base is %" PRId64 ", but exponent is %" PRId64 "\n", a, n);
        exit(1);
    } else if (a == 0 && n == 0) {
        return 1;
    }

    bool sign;
    if ((sign = n < 0)) {
        n = -n;
    }

    double result = _fast_power_r(a, n);
    return (sign) ? 1 / result : result;
}

extern double fast_power_c(int64_t a, int64_t n)
{
    if (a == 0 && n < 0) {
        fprintf(stderr, "Math result not representable: base is %" PRId64 ", but exponent is %" PRId64 "\n", a, n);
        exit(1);
    } else if (a == 0 && n == 0) {
        return 1;
    }

    bool sign;
    if ((sign = n < 0)) {
        n = -n;
    }

    double result = _fast_power_c(a, n);
    return (sign) ? 1 / result : result;
}
