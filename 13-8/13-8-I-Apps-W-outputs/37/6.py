
def get_optimal_program(a, M):
    # Your code here
    return a

def get_total_time(a, M):
    # Your code here
    return 0

if __name__ == '__main__':
    n, M = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_total_time(get_optimal_program(a, M), M))

