# https://practice.geeksforgeeks.org/problems/numbers-with-prime-frequencies-greater-than-or-equal-to-k/0

import operator

def generate_primes():
    primes = [True]*1002
    primes[0] = False
    primes[1] = False
    for index in range(2, 32):
        for i in range(index**2, 1002, index):
            primes[i] = False
    numbers = []
    for index in range(1002):
        if primes[index]:
            numbers.append(index)
    return numbers
    
primes = generate_primes()

for _ in range(int(input())):
    N, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    # count frequencies of numbers
    frequencies = dict.fromkeys(set(arr), 0)
    for num in arr:
        frequencies[num] += 1
        
    # sort the dictionary by key
    frequencies = sorted(frequencies.items(), key = operator.itemgetter(0))
    
    found_one = False
    # go number by number
    for item in frequencies:
        if item[1] >= k and item[1] in primes:
            found_one = True
            print(item[0], end = " ")

    if not found_one:
        print(-1)
    else:
        print()
