# https://practice.geeksforgeeks.org/problems/xor-count-zero-and-one/0
# level: easy


def count_zeros_ones(N):
    # convert to binary and remove 0b
    bin_list = list(bin(N)[2:])
    # return two values
    return bin_list.count('0'), bin_list.count('1')


for t in range(int(input())):
    N = int(input())
    zeros, ones = count_zeros_ones(N)
    # ^ is XOR in python
    print(zeros ^ ones)