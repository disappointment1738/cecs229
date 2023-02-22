def primes(a, b):
    """lists out the prime numbers between a and b, inclusive
    param@ int a: the lower bound
    param@ int b: the upper bound
    """
    # initial checks before running
    if a < 1:
        raise ValueError('a must be non-negative')
    if a > b:
        raise ValueError('a cannot be greater than b')
    # create a list of integers a to b.
    primes = {n for n in range(a, b + 1)}
    # remove 1 from the set, since 1 is not a prime number
    primes.discard(1)
    # include 2 in the set if a <= 2, because 2 is prime
    if a < 2:
        primes.add(2)

    for i in range(2, int(b**0.5 + 1) ):
        for mult in range(i*2, b + 1, i):
            if mult in primes:
                primes.remove(mult)
    return primes

primes(50, 213)