/*
 * [Time-Complexity]: O(k * log^3(p))
 *
 * [Space-Complexity]: O(1)
 *
 *
 * According to Rabin's theorem, the probability that a randomly chosen number a witnesses the simplicity of a
 * composite number is approximately 1/4.
 *
 * Hence, if we check k random numbers a, the probability of accepting a composite number as prime is ~(1/4)^k.
 *
 * The complexity of the algorithm is O(k * log^3(p)), where k is the number of checks.
 *
 */

#include "isprime.h"

/*
 * Fast modulo degree function.
 *
 * Calculates x^y (mod p)
 *
 *      x - is base
 *
 *      y - is exponent
 *
 *      p - is module
 *
 * */
static uint64_t power_mod(uint64_t x, uint64_t y, const uint64_t p)
{
    uint64_t result = 1LLU;
    x &= p;

    while (y) {
        if (y & 1) result = (result * x) % p;
        y >>= 1;  // y / 2
        x = (x * x) % p;
    }

    return result;
}


/*
 * Miller-Rabin Primality Test
 *
 * Tests the number for the possibility of simplicity.
 *
 *      number - is the number to be tested.
 *
 *      d - is an odd number such that n − 1 can be written in the form of d ∗ 2^r
 */
static bool miller_rabin_test(uint64_t d, const uint64_t number)
{
    uint64_t a = 2LLU + (uint64_t)rand() % (number - 4LLU);
    uint64_t x = power_mod(a, d, number);

    if (x == 1LLU || x == number - 1LLU) return true;

    while (d != number - 1LLU) {
        x = (x * x) % number;
        d <<= 1LLU;  // d * 2

        if (x == 1) return false;
        if (x == number - 1LLU) return true;
    }

    return false;
}


/*
 * Probabilistic test of number for simplicity using the Miller-Rabin test
 *
 *      number - is the number to be tested.
 *
 *      k - Number of tests. The larger the number, the less likely it is that a composite number
 *          will be misidentified as a prime number. (1/4)^k
 */
extern bool is_prime(const uint64_t number, uint16_t k)
{
    if (number < 2LLU || number == 4) return false;
    if (number <= 3) return true;

    uint64_t d = number - 1;
    while ((d & 1LLU) == 0) d >>= 1LLU;

    while (k-- != 0) {
        if (!miller_rabin_test(d, number)) return false;
    }

    return true;
}
