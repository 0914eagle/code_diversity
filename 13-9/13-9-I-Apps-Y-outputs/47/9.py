
def get_input():
    m = int(input())
    m_list = list(map(int, input().split()))
    n = int(input())
    n_list = list(map(int, input().split()))
    return m, m_list, n, n_list

def symmetric_difference(m_list, n_list):
    return list(set(m_list).symmetric_difference(set(n_list)))

def main():
    m, m_list, n, n_list = get_input()
    result = symmetric_difference(m_list, n_list)
    for num in sorted(result):
        print(num)

if __name__ == '__main__':
    main()

