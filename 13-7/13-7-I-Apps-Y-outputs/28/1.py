
def get_number_of_ways(n, k):
    if n == 1:
        return k
    if n == 2:
        return k * (k - 1)
    return (k - 1) * get_number_of_ways(n - 1, k) + k * get_number_of_ways(n - 2, k)

def main():
    n, k = map(int, input().split())
    print(get_number_of_ways(n, k))

if __name__ == '__main__':
    main()

