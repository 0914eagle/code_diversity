
def get_input():
    return int(input())

def calculate_carryless_multiplication(a, b):
    result = 0
    for i in range(len(str(a))):
        for j in range(len(str(b))):
            result += int(str(a)[-i-1]) * int(str(b)[-j-1])
    return result

def find_smallest_positive_integer(n):
    for i in range(1, n+1):
        if calculate_carryless_multiplication(i, i) == n:
            return i
    return -1

if __name__ == '__main__':
    n = get_input()
    print(find_smallest_positive_integer(n))

