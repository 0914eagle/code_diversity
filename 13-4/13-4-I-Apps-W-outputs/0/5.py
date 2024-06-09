
def get_good_pairs(n, a):
    count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if a[i] & a[j] == a[i] and a[i] ^ a[j] == a[j]:
                count += 1
    return count

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(get_good_pairs(n, a))

if __name__ == '__main__':
    main()

