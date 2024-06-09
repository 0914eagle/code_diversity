
def f(string, T):
    result = ""
    for char in string:
        result += T[ord(char) - ord('a')]
    return result

def solve(S, T, K, M, m_list):
    password = S
    for i in range(K):
        password = f(password, T)
    result = []
    for i in range(M):
        result.append(password[m_list[i] - 1])
    return result

if __name__ == '__main__':
    S = input()
    T = input().split()
    K = int(input())
    M = int(input())
    m_list = list(map(int, input().split()))
    print(*solve(S, T, K, M, m_list))

