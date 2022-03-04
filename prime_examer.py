
def is_prime(number: int) -> bool:
    n = 1000
    is_prime = [True] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    primes = [x for x in range(2, n + 1) if is_prime[x]]
    if number in primes:
        return True
    return False
