#ifndef MATH_PRIME_NUMBERS_SCHOOL_METHOD_H
#define MATH_PRIME_NUMBERS_SCHOOL_METHOD_H

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

/*
 * The function checks number for simplicity in time O(√n)
 *
 * Checks n, whether n is divisible by 2 or 3, and then checks all numbers of the form 6k ± 1 <= √n
 *
 */
extern bool is_prime(const uint64_t number);

#endif  // MATH_PRIME_NUMBERS_SCHOOL_METHOD_H
