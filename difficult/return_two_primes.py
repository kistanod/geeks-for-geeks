# https://practice.geeksforgeeks.org/problems/return-two-prime-numbers/0
# level:difficult


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
    # get a list of only prime numbers
    result = []
    for number, is_prime in enumerate(primes):
        if is_prime:
            result.append(number)
    return result


# answer will always exist
def solve(num):
    # get primes digits
    primes = get_primes(num)
    # from beginning and end
    for i in range(len(primes)):
        for j in range(len(primes)-1, 0, -1):
            # if primes result in input
            if primes[i] + primes[j] == num:
                # return result
                return "{} {}".format(primes[i], primes[j])


for t in range(int(input())):
    print(solve(int(input())))


