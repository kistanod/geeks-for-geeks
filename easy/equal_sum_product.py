# https://practice.geeksforgeeks.org/problems/equal-sum-and-product/0
# level: easy


def product(arr):
    result = 1
    for item in arr:
        result *= item
    return result


def solve(arr):
    count = 0
    for length in range(1, len(arr) + 1):
        for index in range(0, len(arr)):
            temp = arr[index:index + length]
            if length == len(temp):
                if sum(temp) == product(temp):
                    count += 1
    return count


for t in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    print(solve(arr))