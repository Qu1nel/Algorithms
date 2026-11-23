#include "isprime.h"

#include <assert.h>

static bool trial(uint64_t n)
{
    if (n < 2) return false;
    for (uint64_t d = 2; d <= n / d; ++d) {
        if (n % d == 0) return false;
    }
    return true;
}

int main(void)
{
    srand(42);
    for (uint64_t n = 0; n < 3000; ++n) {
        assert(is_prime(n, 16) == trial(n));
    }
    assert(!is_prime(17, 0));
    assert(!is_prime(561, 24));
    assert(!is_prime(UINT64_MAX, 24));
    assert(!is_prime(UINT64_C(18446744030759878681), 24));
    assert(is_prime(UINT64_C(18446744073709551557), 24));
    return 0;
}
