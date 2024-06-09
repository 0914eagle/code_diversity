
def f(s):
    # Your code here
    return s

def f1(s, k):
    # Your code here
    return s

def f2(s, m):
    # Your code here
    return s

if __name__ == '__main__':
    s = input()
    k = int(input())
    m = int(input())
    m_list = list(map(int, input().split()))
    result = []
    for i in range(m):
        result.append(s[m_list[i] - 1])
    print(*result, sep='\n')

