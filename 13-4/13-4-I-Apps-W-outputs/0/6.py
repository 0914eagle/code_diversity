
def get_good_pairs(n, a):
    count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if a[i] & a[j] == a[i] and a[i] ^ a[j] == a[j]:
                count += 1
    return count

def get_lever(n, a):
    return get_good_pairs(n, a)

def get_rock(n, a):
    return get_good_pairs(n, a)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(get_lever(n, a))
        print(get_rock(n, a))

