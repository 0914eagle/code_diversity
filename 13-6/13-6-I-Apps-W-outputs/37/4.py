
def get_binary_representation(x, n):
    return [int(i) for i in bin(x)[2:].zfill(n)]

def get_difference_in_bits(x, y, n):
    return sum([int(i) for i in bin(x ^ y)[2:].zfill(n)])

def get_potential_friends(x_list, k):
    n = len(x_list)
    friend_pairs = []
    for i in range(n):
        for j in range(i+1, n):
            if get_difference_in_bits(x_list[i], x_list[j], n) <= k:
                friend_pairs.append((i, j))
    return len(set(friend_pairs))

def main():
    n, m, k = map(int, input().split())
    x_list = []
    for i in range(m+1):
        x_list.append(int(input()))
    print(get_potential_friends(x_list, k))

if __name__ == '__main__':
    main()

