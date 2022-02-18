
def is_prime(number):
    n = 1000
    IsPrime = [True] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if IsPrime[i]:
            for j in range(i * i, n + 1, i):
                IsPrime[j] = False
    primes = [x for x in range(2, n + 1) if IsPrime[x]]
    if number in primes:
        return True
    return False
