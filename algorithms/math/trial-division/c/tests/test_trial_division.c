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
    for (uint64_t n = 0; n < 3000; ++n) {
        assert(is_prime(n) == trial(n));
    }
    assert(!is_prime(49));
    assert(!is_prime(UINT64_MAX));
    assert(!is_prime(UINT64_C(1000003) * UINT64_C(1000003)));
    assert(is_prime(997));
    return 0;
}
