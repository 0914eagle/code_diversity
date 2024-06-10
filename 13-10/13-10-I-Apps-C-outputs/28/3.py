
def get_optimal_strategy(n, d, b, a):
    # Your code here
    return ...

def main():
    n, d, b = map(int, input().split())
    a = list(map(int, input().split()))
    result = get_optimal_strategy(n, d, b, a)
    print(result)

if __name__ == '__main__':
    main()

