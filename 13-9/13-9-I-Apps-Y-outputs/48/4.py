
def get_min_snacks(A, B):
    return (A + B) // 2

def main():
    A, B = map(int, input().split())
    print(get_min_snacks(A, B))

if __name__ == '__main__':
    main()

