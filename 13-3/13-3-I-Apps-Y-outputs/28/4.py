
def get_symmetric_difference(m, n):
    return list(sorted(m.union(n) - m.intersection(n)))

def main():
    m_count = int(input())
    m = set(map(int, input().split()))
    n_count = int(input())
    n = set(map(int, input().split()))
    symmetric_difference = get_symmetric_difference(m, n)
    for num in symmetric_difference:
        print(num)

if __name__ == '__main__':
    main()

