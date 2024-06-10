
def get_optimal_program(a, M):
    # Your code here
    return a

def get_total_lit_time(a, M):
    # Your code here
    return 0

if __name__ == '__main__':
    n, M = map(int, input().split())
    a = list(map(int, input().split()))
    optimal_program = get_optimal_program(a, M)
    total_lit_time = get_total_lit_time(optimal_program, M)
    print(total_lit_time)

