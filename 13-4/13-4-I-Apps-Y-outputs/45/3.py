
def get_input():
    return list(map(int, input().split()))

def can_multiply(a, b):
    return 1 <= a <= 9 and 1 <= b <= 9

def multiply(a, b):
    if can_multiply(a, b):
        return a * b
    else:
        return -1

if __name__ == '__main__':
    a, b = get_input()
    print(multiply(a, b))

