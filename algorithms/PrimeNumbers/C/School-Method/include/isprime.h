#ifndef PRIMENUMBERTEST_IS_PRIME_H
#define PRIMENUMBERTEST_IS_PRIME_H

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

#endif
