
def carryless_multiplication(a, b):
    result = 0
    for i in range(len(a)):
        for j in range(len(b)):
            result += a[i] * b[j]
    return result % 10

def find_solution(n):
    for i in range(1, n+1):
        if carryless_multiplication(str(i), str(i)) == n:
            return i
    return -1

if __name__ == '__main__':
    n = int(input())
    print(find_solution(n))

