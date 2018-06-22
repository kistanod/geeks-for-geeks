# https://practice.geeksforgeeks.org/problems/element-that-appears-once-where-every-element-occurs-twice/0
# level: easy

for t in range(int(input())):
    # collect data
    N = int(input())
    arr = list(map(int, input().split()))
    # make a set out of arr
    arr_set = list(set(arr))
    # sum of set*2
    # subtract the sum of list
    result = (sum(arr_set) * 2) - sum(arr)
    print(result)