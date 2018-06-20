# https://practice.geeksforgeeks.org/problems/find-prime-numbers-in-a-range/0
# level: difficult


def get_primes(N):
    # make array of size N
    primes = [True]*N
    primes[0] = False  # 1 and 0
    primes[1] = False  # are not primes:D
    # for every digit up to sqrt(N)
    for num in range(2, int(N**(1/2))):
        if primes[num]:  # if true
            # multiples of that number
            # are not primes
            for i in range(num**2, N, num):
                primes[i] = False
    return primes


for t in range(int(input())):
    for index, prime in enumerate(get_primes(int(input()))):
        if prime:
            print(index, end=" ")