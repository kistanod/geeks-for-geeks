# https://practice.geeksforgeeks.org/problems/sorting-elements-of-an-array-by-frequency/0
# level: difficult


def freq_sort(lst):
    # make a list of unique digits
    arr = list(set(lst))
    # make a dict out of values for arr
    freq_list = {key: 0 for key in arr}
    # run through all the values and tally up
    for item in lst:
        freq_list[item] += 1
    # sort the dict and print values
    for w in sorted(freq_list, key=freq_list.get, reverse=True):
        for i in range(freq_list[w]):
            print(w, end=" ")
    print()


# collect the input
for t in range(int(input())):
    N = int(input())  # requires N for java or c problems
    freq_sort(list(map(int, input().split())))