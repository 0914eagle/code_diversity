
def can_multiply(a, b):
    if a in range(1, 10) and b in range(1, 10):
        return True
    else:
        return False

def multiply(a, b):
    if can_multiply(a, b):
        return a * b
    else:
        return -1

if __name__ == '__main__':
    a, b = map(int, input().split())
    result = multiply(a, b)
    print(result)

