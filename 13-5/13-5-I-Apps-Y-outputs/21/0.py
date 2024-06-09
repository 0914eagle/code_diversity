
def is_increasing(seq):
    return all(seq[i] < seq[i+1] for i in range(len(seq)-1))

def is_decreasing(seq):
    return all(seq[i] > seq[i+1] for i in range(len(seq)-1))

def find_increasing_and_decreasing(seq):
    n = len(seq)
    if n == 0:
        return []
    if n == 1:
        return [0]
    if is_increasing(seq):
        return [0] * n
    if is_decreasing(seq):
        return [1] * n
    for i in range(1, n-1):
        if seq[i] < seq[i-1] and seq[i] < seq[i+1]:
            return [0] * i + [1] + [0] * (n-i-1)
        if seq[i] > seq[i-1] and seq[i] > seq[i+1]:
            return [1] * i + [0] + [1] * (n-i-1)
    return []

def main():
    n = int(input())
    seq = list(map(int, input().split()))
    res = find_increasing_and_decreasing(seq)
    if not res:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, res)))

if __name__ == '__main__':
    main()

