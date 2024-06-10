
def get_operations(a, b):
    if a == b:
        return 0
    
    operations = 0
    while a != b:
        if a % 2 == 0:
            a //= 2
        elif a % 4 == 0:
            a //= 4
        elif a % 8 == 0:
            a //= 8
        else:
            return -1
        operations += 1
    
    return operations

def main():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        print(get_operations(a, b))

if __name__ == '__main__':
    main()

