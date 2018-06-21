# https://practice.geeksforgeeks.org/problems/sum-of-bit-differences/0
# level : medium

from itertools import combinations


def make_pairs(input_lst):
    # make pairs of size 2
    return list(combinations(input_lst, 2))


def count_dif_bits(pairs):
    count = 0
    # for every pair
    for pair in list(pairs):
        # turn into binary
        # make same length
        # reverse it
        a = bin(pair[0])[2:].zfill(5)[::-1]
        b = bin(pair[1])[2:].zfill(5)[::-1]
        # count the bits
        count += get_dif_count(a, b)
        count += get_dif_count(b, a)
    return count


def get_dif_count(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    return count


for t in range(int(input())):
    input()  # dump the input
    lst = list(map(int, input().split()))
    print(count_dif_bits(make_pairs(lst)))