
def get_different_bits(x, y):
    return bin(x ^ y).count("1")

def get_friends(n, m, k, armies):
    friends = 0
    for i in range(m):
        for j in range(i + 1, m):
            if get_different_bits(armies[i], armies[j]) <= k:
                friends += 1
    return friends

def main():
    n, m, k = map(int, input().split())
    armies = []
    for i in range(m + 1):
        armies.append(int(input()))
    print(get_friends(n, m, k, armies))

if __name__ == '__main__':
    main()

