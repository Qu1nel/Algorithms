/*
 * [Time-Complexity]: O(√n)
 *
 * [Space-Complexity]: O(1)
 *
 * The test is based on the fact that all prime numbers greater than 3 are of the form 6k ± 1, where k is any integer
 * greater than 0.
 *
 * */

#include "isprime.h"


/*
 * The function checks number for simplicity in time O(√n)
 *
 * Checks n, whether n is divisible by 2 or 3, and then checks all numbers of the form 6k ± 1 <= √n
 *
 */
extern bool is_prime(const uint64_t number)
{
    if (number <= 3) return number > 1;
    if (number % 2 == 0 || number % 3 == 0) return false;

    for (register uint64_t i = 5; i * i <= number; i += 6) {
        if ((number % i == 0) || (number % (i + 2) == 0)) return false;
    }
    return true;
}
