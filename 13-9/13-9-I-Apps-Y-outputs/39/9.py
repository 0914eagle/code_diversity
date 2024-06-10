
def get_input():
    return [int(x) for x in input().split()]

def is_multiple_of_a(n, a):
    return n % a == 0

def find_numbers(a, b, c):
    for i in range(1, b):
        if is_multiple_of_a(i, a) and (i + c) % b == 0:
            return True
    return False

def main():
    a, b, c = get_input()
    if find_numbers(a, b, c):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

