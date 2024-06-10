
def get_symmetric_difference(m, n):
    return list(set(m).symmetric_difference(set(n)))

def main():
    m_count = int(input())
    m = set(map(int, input().split()))
    n_count = int(input())
    n = set(map(int, input().split()))
    symmetric_difference = get_symmetric_difference(m, n)
    print(*symmetric_difference, sep='\n')

if __name__ == '__main__':
    main()

