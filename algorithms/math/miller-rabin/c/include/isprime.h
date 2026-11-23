#ifndef MATH_PRIME_NUMBERS_MILLER_RABIN_H
#define MATH_PRIME_NUMBERS_MILLER_RABIN_H

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

/*
 * Test a candidate with k Miller–Rabin rounds.
 * False means composite, below 2, or an invalid round count (k = 0).
 * True means the number passed every round. See the README for the
 * error bound under independent uniform sampling.
 */
extern bool is_prime(const uint64_t number, uint16_t k);

#endif  // MATH_PRIME_NUMBERS_MILLER_RABIN_H
