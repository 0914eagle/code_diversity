
def get_min_operations(a, b):
    if a == b:
        return 0
    
    operations = 0
    while a != b:
        if a % 2 == 0 and b % 2 == 0:
            a //= 2
            b //= 2
        elif a % 4 == 0 and b % 4 == 0:
            a //= 4
            b //= 4
        elif a % 8 == 0 and b % 8 == 0:
            a //= 8
            b //= 8
        else:
            return -1
        operations += 1
    
    return operations

def main():
    num_test_cases = int(input())
    for _ in range(num_test_cases):
        a, b = map(int, input().split())
        print(get_min_operations(a, b))

if __name__ == '__main__':
    main()

