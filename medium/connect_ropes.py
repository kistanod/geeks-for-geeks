# https://practice.geeksforgeeks.org/problems/minimum-cost-of-ropes/0
# level: medium


def connect_ropes(lengths):
    # pass the temp(no need to sort)
    temp = []

    if len(lengths) == 1:
        # sum of temp, not lengths
        return sum(temp)

    # because it is sorted, i can just add two
    # at the end
    lengths.append(lengths[0] + lengths[1])

    # add that value to temp
    temp.append(lengths[0] + lengths[1])

    # delete first two!
    lengths.remove(lengths[0])
    lengths.remove(lengths[0])

    # return the sorted vesion of lengths and regualr temp
    return connect_ropes(list(sorted(lengths)), temp)


# accept all inputs and then call the function
for t in range(int(input())):
    length = input()
    ropes = list(sorted(list(map(int, input().split()))))
    print(connect_ropes(ropes))
