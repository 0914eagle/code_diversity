
def get_binary_representation(x, n):
    return [int(i) for i in bin(x)[2:].zfill(n)]

def get_difference_in_bits(x1, x2, n):
    return sum([int(i) for i in bin(x1 ^ x2)[2:].zfill(n)])

def get_potential_friends(x, m, k):
    friends = 0
    for i in range(m):
        if get_difference_in_bits(x[i], x[m], k) <= k:
            friends += 1
    return friends

def main():
    n, m, k = map(int, input().split())
    x = [int(input()) for _ in range(m + 1)]
    print(get_potential_friends(x, m, k))

if __name__ == '__main__':
    main()

