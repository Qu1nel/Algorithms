#include "fastpow.h"

#include <assert.h>
#include <math.h>

static void check_power(int64_t base, int64_t exponent, double expected)
{
    assert(fabs(fast_power_r(base, exponent) - expected) < 1e-12);
    assert(fabs(fast_power_c(base, exponent) - expected) < 1e-12);
}

int main(void)
{
    check_power(0, 0, 1.0);
    check_power(5, 0, 1.0);
    check_power(0, 7, 0.0);
    check_power(-3, 5, -243.0);
    check_power(-3, 6, 729.0);
    check_power(2, -10, 1.0 / 1024.0);
    check_power(-1, INT64_MIN, 1.0);
    check_power(-1, INT64_MAX, -1.0);
    check_power(INT64_MAX, 2, 0x1p126);
    return 0;
}
