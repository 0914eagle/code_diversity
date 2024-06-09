
def get_pairs(a, b, c):
    pairs = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] == b[j] and a[j] == c[i]:
                pairs += 1
    return pairs

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    print(get_pairs(a, b, c))

if __name__ == '__main__':
    main()

