
def is_divisible_by(n, d):
    return n % d == 0

def get_min_operations(a, b):
    if a == b:
        return 0
    
    operations = []
    for i in range(1, 4):
        if is_divisible_by(a, 2**i) and a * 2**i == b:
            operations.append(i)
    
    if not operations:
        return -1
    
    return min(operations)

def main():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        print(get_min_operations(a, b))

if __name__ == '__main__':
    main()

