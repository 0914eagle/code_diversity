
def is_valid_input(n, a, b):
    if n == 0:
        return False
    if a == b:
        return True
    for k in range(1, n // 2 + 1):
        if a[:k] == b[n-k:] and a[k:] == b[:n-k]:
            return True
    return False

def main():
    num_test_cases = int(input())
    for i in range(num_test_cases):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        if is_valid_input(n, a, b):
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()

