
def is_increasing(sequence):
    return all(sequence[i] <= sequence[i+1] for i in range(len(sequence)-1))

def recover_sequence(a, b):
    n = len(a)
    k = len(b)
    if n == k:
        return a
    if n < k:
        return None
    sequence = a[:]
    for i in range(k):
        zero_index = sequence.index(0)
        sequence[zero_index] = b[i]
    return sequence if is_increasing(sequence) else None

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = recover_sequence(a, b)
    if result:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

