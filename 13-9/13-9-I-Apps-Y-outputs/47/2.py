
def get_input():
    m = int(input())
    m_set = set(map(int, input().split()))
    n = int(input())
    n_set = set(map(int, input().split()))
    return m_set, n_set

def symmetric_difference(m_set, n_set):
    return m_set.union(n_set).difference(m_set.intersection(n_set))

def main():
    m_set, n_set = get_input()
    symmetric_difference = symmetric_difference(m_set, n_set)
    for num in sorted(symmetric_difference):
        print(num)

if __name__ == '__main__':
    main()

