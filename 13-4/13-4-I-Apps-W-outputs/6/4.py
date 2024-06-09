
def find_optimal_time(t_s, t_f, t, n, visitors):
    # Find the time when the receptionist is free
    free_time = t_f - t
    
    # Find the time when the last visitor arrives
    last_visitor_time = visitors[-1]
    
    # Find the time when Vasya can arrive to be served immediately
    optimal_time = max(free_time, last_visitor_time)
    
    return optimal_time

def main():
    t_s, t_f, t = map(int, input().split())
    n = int(input())
    visitors = sorted([int(x) for x in input().split()])
    
    print(find_optimal_time(t_s, t_f, t, n, visitors))

if __name__ == '__main__':
    main()

