def freq_sort(lst):
    arr = list(range(1,61))
    freq_list = {key: 0 for key in arr}
    for item in lst:
        freq_list[item] += 1
    for w in sorted(freq_list, key=freq_list.get, reverse=True):
        if freq_list[w] == 0:
            break
        for i in range(freq_list[w]):
            print(w, end=" ")
    print()


for t in range(int(input())):
    N = int(input())
    freq_sort(list(map(int, input().split())))