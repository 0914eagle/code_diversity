
def get_input():
    M = int(input())
    m_set = set(map(int, input().split()))
    N = int(input())
    n_set = set(map(int, input().split()))
    return M, m_set, N, n_set

def symmetric_difference(M, m_set, N, n_set):
    return sorted(m_set ^ n_set)

def main():
    M, m_set, N, n_set = get_input()
    result = symmetric_difference(M, m_set, N, n_set)
    for num in result:
        print(num)

if __name__ == '__main__':
    main()

