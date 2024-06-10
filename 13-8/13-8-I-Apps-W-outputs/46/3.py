
def get_pairs_count(a, k):
    count = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] * a[j] == k:
                count += 1
    return count

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_pairs_count(a, k))

if __name__ == '__main__':
    main()

