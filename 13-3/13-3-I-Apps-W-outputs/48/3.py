
def get_increasing_sequence(b):
    n = len(b)
    a = [0] * n
    a[0] = b[0]
    for i in range(1, n):
        a[i] = a[i-1] ^ b[i]
    return a

def get_valid_permutation(b):
    n = len(b)
    a = get_increasing_sequence(b)
    for i in range(n):
        for j in range(i+1, n):
            if a[i] > a[j]:
                b[i], b[j] = b[j], b[i]
                a = get_increasing_sequence(b)
                if a == sorted(a):
                    return b
                else:
                    b[i], b[j] = b[j], b[i]
    return None

if __name__ == '__main__':
    n = int(input())
    b = list(map(int, input().split()))
    result = get_valid_permutation(b)
    if result is None:
        print("No")
    else:
        print("Yes")
        print(" ".join(map(str, result)))

