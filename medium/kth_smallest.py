import heapq

for t in range(int(input())):
    # collect input
    size = int(input())
    lst = list(map(int, input().split()))
    k = int(input())
    # build the heap
    heapq.heapify(lst)
    # remove k-1 elements
    for i in range(k-1):
        heapq.heappop(lst)
    # print kth smallest
    print(heapq.heappop(lst))