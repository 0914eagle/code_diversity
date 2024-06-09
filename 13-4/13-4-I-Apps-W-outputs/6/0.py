
def find_optimal_time(t_s, t_f, t, n, visitors):
    # Find the time when the receptionist is free
    free_time = (t_f - 1) - (n - 1) * t
    
    # Find the time when Vasya should arrive
    arrival_time = free_time - t
    
    return arrival_time

def main():
    t_s, t_f, t = map(int, input().split())
    n = int(input())
    visitors = list(map(int, input().split()))
    
    print(find_optimal_time(t_s, t_f, t, n, visitors))

if __name__ == '__main__':
    main()

