
def f1(n, a):
    # find the longest good sequence
    max_length = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[j] - a[i] > 1 and all(gcd(a[j] - a[i], a[k] - a[i]) > 1 for k in range(i+1, j)):
                max_length = max(max_length, j - i + 1)
    return max_length

def f2(n, a):
    # find all good sequences
    sequences = []
    for i in range(n):
        for j in range(i+1, n):
            if a[j] - a[i] > 1 and all(gcd(a[j] - a[i], a[k] - a[i]) > 1 for k in range(i+1, j)):
                sequences.append(a[i:j+1])
    return sequences

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(f1(n, a))
    print(f2(n, a))

