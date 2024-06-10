
def get_optimal_program(a, M):
    # Your code here
    return a

def main():
    n, M = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_optimal_program(a, M))

if __name__ == '__main__':
    main()

