
def is_valid_test_case(n, a, b):
    if a == b:
        return True
    
    for k in range(1, n // 2 + 1):
        a_prefix = a[:k]
        a_suffix = a[k:]
        if a_prefix == a_suffix:
            continue
        a_prefix.reverse()
        a_suffix.reverse()
        a = a_prefix + a_suffix
        if a == b:
            return True
    
    return False

def main():
    num_test_cases = int(input())
    for _ in range(num_test_cases):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        if is_valid_test_case(n, a, b):
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()

