
def get_min_snacks(A, B):
    # Find the smallest common multiple of A and B
    smallest_common_multiple = A * B // math.gcd(A, B)
    return smallest_common_multiple

def main():
    A, B = map(int, input().split())
    print(get_min_snacks(A, B))

if __name__ == '__main__':
    main()

