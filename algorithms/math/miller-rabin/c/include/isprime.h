#ifndef MATH_PRIME_NUMBERS_MILLER_RABIN_H
#define MATH_PRIME_NUMBERS_MILLER_RABIN_H

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

/*
 * Probabilistic test of number for simplicity using the Miller-Rabin test
 *
 *      number - is the number to be tested.
 *
 *      k - Number of tests. The larger the number, the less likely it is that a composite number
 *          will be misidentified as a prime number. (1/4)^k
 */
extern bool is_prime(const uint64_t number, uint16_t k);

#endif  // MATH_PRIME_NUMBERS_MILLER_RABIN_H
