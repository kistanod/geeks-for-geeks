# https://practice.geeksforgeeks.org/viewSol.php?subId=5908112&pid=495&user=kistanod
# level : medium


def num_to_url(input_num):
    base_62 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    result = ""
    while input_num != 0:
        result += base_62[input_num % 62]
        input_num = input_num // 62
    return result[::-1]


def url_to_num(input_url):
    base_62 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    result = 0
    for item in list(input_url):
        result *= 62
        result += base_62.find(item)
    return result


for t in range(int(input())):
    url = num_to_url(int(input()))
    num = url_to_num(url)
    print(url)
    print(num)