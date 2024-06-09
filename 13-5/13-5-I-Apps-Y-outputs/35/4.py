
def get_triplets(n, k):
    count = 0
    for a in range(1, n+1):
        for b in range(a, n+1):
            for c in range(b, n+1):
                if (a+b)%k == 0 and (b+c)%k == 0 and (c+a)%k == 0:
                    count += 1
    return count

def main():
    n, k = map(int, input().split())
    print(get_triplets(n, k))

if __name__ == '__main__':
    main()

