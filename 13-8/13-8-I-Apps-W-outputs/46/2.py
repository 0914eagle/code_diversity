
def read_input():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    return n, k, a

def count_pairs(n, k, a):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            x = a[i] * a[j]
            if x ** (1/k) % 1 == 0:
                count += 1
    return count

def main():
    n, k, a = read_input()
    print(count_pairs(n, k, a))

if __name__ == '__main__':
    main()

