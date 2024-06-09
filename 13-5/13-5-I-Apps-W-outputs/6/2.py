
def is_valid_test_case(n, a, b):
    # Your code here
    return True

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        if is_valid_test_case(n, a, b):
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()

