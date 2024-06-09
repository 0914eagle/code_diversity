
def is_valid_test_case(a, b):
    n = len(a)
    for i in range(1, int(n/2)+1):
        if a[:i] == b[n-i:] and a[i:] == b[:n-i]:
            return True
    return False

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        if is_valid_test_case(a, b):
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()

