
def read_input():
    A = input()
    P, M = map(int, input().split())
    return A, P, M

def is_valid_expression(A):
    if 'x' not in A:
        return False
    if 'x' * 2 in A:
        return False
    if '(' in A and ')' not in A:
        return False
    if ')' in A and '(' not in A:
        return False
    return True

def solve(A, P, M):
    if not is_valid_expression(A):
        return -1
    x = 0
    while True:
        if (A % M) == P:
            return x
        x += 1
        A = A + M
    return -1

if __name__ == '__main__':
    A, P, M = read_input()
    print(solve(A, P, M))

