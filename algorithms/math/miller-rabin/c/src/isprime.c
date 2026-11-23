/*
 * Miller–Rabin primality test for uint64_t.
 *
 * [Time-Complexity]: O(k log n) modular multiplications
 * [Space-Complexity]: O(1) machine words
 */

#include "isprime.h"

/* a and b are already reduced. Subtract before adding to avoid overflow. */
static uint64_t add_mod(uint64_t a, uint64_t b, uint64_t modulus)
{
    return a >= modulus - b ? a - (modulus - b) : a + b;
}

static uint64_t multiply_mod(uint64_t a, uint64_t b, uint64_t modulus)
{
    uint64_t result = 0;
    while (b != 0) {
        if (b % 2 != 0) result = add_mod(result, a, modulus);
        b /= 2;
        if (b != 0) a = add_mod(a, a, modulus);
    }
    return result;
}

static uint64_t power_mod(uint64_t base, uint64_t exponent, uint64_t modulus)
{
    uint64_t result = 1;
    while (exponent != 0) {
        if (exponent % 2 != 0) result = multiply_mod(result, base, modulus);
        exponent /= 2;
        if (exponent != 0) base = multiply_mod(base, base, modulus);
    }
    return result;
}

static uint64_t random_bit(void)
{
    int draw;
    do {
        draw = rand();
    } while (RAND_MAX % 2 == 0 && draw == RAND_MAX);
    return draw >= RAND_MAX / 2 + RAND_MAX % 2 ? UINT64_C(1) : UINT64_C(0);
}

/* Rejection sampling covers the full range even when RAND_MAX is small. */
static uint64_t random_below(uint64_t limit)
{
    uint64_t candidate;
    do {
        candidate = 0;
        for (uint64_t bits = limit - 1; bits != 0; bits /= 2) {
            candidate = (candidate << 1) | random_bit();
        }
    } while (candidate >= limit);
    return candidate;
}

static bool miller_rabin_test(uint64_t d, unsigned shifts, uint64_t number)
{
    uint64_t a = 2 + random_below(number - 3);
    uint64_t x = power_mod(a, d, number);

    if (x == 1 || x == number - 1) return true;
    for (unsigned r = 1; r < shifts; ++r) {
        x = multiply_mod(x, x, number);
        if (x == 1) return false;
        if (x == number - 1) return true;
    }
    return false;
}

bool is_prime(const uint64_t number, uint16_t k)
{
    if (k == 0 || number < 2) return false;
    if (number <= 3) return true;
    if (number % 2 == 0) return false;

    uint64_t d = number - 1;
    unsigned shifts = 0;
    while (d % 2 == 0) {
        d /= 2;
        ++shifts;
    }

    for (uint16_t round = 0; round < k; ++round) {
        if (!miller_rabin_test(d, shifts, number)) return false;
    }
    return true;
}
