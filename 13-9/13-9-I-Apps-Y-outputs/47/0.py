
def get_input():
    M = int(input())
    m_list = list(map(int, input().split()))
    N = int(input())
    n_list = list(map(int, input().split()))
    return M, m_list, N, n_list

def symmetric_difference(M, m_list, N, n_list):
    m_set = set(m_list)
    n_set = set(n_list)
    return list(m_set.symmetric_difference(n_set))

def main():
    M, m_list, N, n_list = get_input()
    symmetric_difference = symmetric_difference(M, m_list, N, n_list)
    for num in symmetric_difference:
        print(num)

if __name__ == '__main__':
    main()

