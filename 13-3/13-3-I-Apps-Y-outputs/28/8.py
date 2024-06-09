
def get_symmetric_difference(m, n):
    return list(sorted(set(m) ^ set(n)))

def main():
    m_count = int(input())
    m = set(map(int, input().split()))
    n_count = int(input())
    n = set(map(int, input().split()))
    result = get_symmetric_difference(m, n)
    print(*result, sep='\n')

if __name__ == '__main__':
    main()

