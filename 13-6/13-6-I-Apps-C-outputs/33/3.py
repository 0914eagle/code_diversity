
def get_input():
    return int(input())

def carryless_multiplication(a, b):
    result = 0
    for i in range(len(str(a))):
        result += int(str(a)[i]) * int(str(b)[i])
    return result

def find_solution(n):
    for i in range(1, n):
        if carryless_multiplication(i, i) == n:
            return i
    return -1

if __name__ == '__main__':
    n = get_input()
    print(find_solution(n))

