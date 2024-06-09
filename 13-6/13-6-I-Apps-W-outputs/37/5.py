
def get_binary_representation(x, n):
    return [int(i) for i in bin(x)[2:].zfill(n)]

def get_difference_in_bits(x, y, n):
    return sum([int(i) for i in bin(x ^ y)[2:].zfill(n)])

def get_friends(x_list, n, k):
    friends = 0
    for i in range(len(x_list)):
        for j in range(i+1, len(x_list)):
            if get_difference_in_bits(x_list[i], x_list[j], n) <= k:
                friends += 1
    return friends

def main():
    n, m, k = map(int, input().split())
    x_list = []
    for i in range(m+1):
        x_list.append(int(input()))
    print(get_friends(x_list, n, k))

if __name__ == '__main__':
    main()

