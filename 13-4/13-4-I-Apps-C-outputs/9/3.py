
def carryless_multiplication(a, b):
    result = 0
    for i in range(len(str(a))):
        for j in range(len(str(b))):
            result += int(str(a)[-i-1]) * int(str(b)[-j-1])
        result = result % 10
    return result

def find_solution(N):
    for a in range(1, 1000000000):
        if carryless_multiplication(a, a) == N:
            return a
    return -1

N = int(input())
print(find_solution(N))

