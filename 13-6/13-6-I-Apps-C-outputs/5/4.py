
def f(string, mapping):
    result = ""
    for char in string:
        result += mapping[char]
    return result

def main():
    S = input()
    T_a = input()
    T_b = input()
    K = int(input())
    M = int(input())
    m_list = list(map(int, input().split()))

    mapping = {}
    for i in range(26):
        mapping[chr(i + 97)] = T_a[i] + T_b[i]

    password = S
    for i in range(K):
        password = f(password, mapping)

    for m in m_list:
        print(password[m - 1])

if __name__ == '__main__':
    main()

