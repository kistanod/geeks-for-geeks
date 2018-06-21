# https://practice.geeksforgeeks.org/problems/count-of-subarrays/0
# level: medium


def count_sub_arr(arr, k):
    count = 0
    # with n**2 complexity
    for i in range(len(arr)):
        for j in range(len(arr) + 1):
            if i < j and max(arr[i:j]) > k:
                count += 1
    return count


for t in range(int(input())):
    # take input
    N, K = map(int, input().split())
    input_arr = list(map(int, input().split()))
    # solve
    print(count_sub_arr(input_arr, K))