
def find_min_positive_divisible(l, r, d):
    for i in range(l, r+1):
        if i % d == 0 and i not in range(l, r+1):
            return i
    return -1

def main():
    q = int(input())
    for _ in range(q):
        l, r, d = map(int, input().split())
        print(find_min_positive_divisible(l, r, d))

if __name__ == '__main__':
    main()

