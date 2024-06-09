
def f(string, mapping):
    result = ""
    for char in string:
        result += mapping[char]
    return result

def find_password(S, T, K, M, m):
    mapping = {}
    for i in range(len(T)):
        mapping[chr(ord('a') + i)] = T[i]
    password = f(S, mapping)
    for i in range(K-1):
        password = f(password, mapping)
    result = []
    for i in range(M):
        result.append(password[m[i]-1])
    return result

if __name__ == '__main__':
    S = input()
    T = input().split()
    K = int(input())
    M = int(input())
    m = list(map(int, input().split()))
    print(*find_password(S, T, K, M, m))

