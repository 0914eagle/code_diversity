
def find_optimal_time(t_s, t_f, t, n, visitors):
    # Find the time when the receptionist is free
    free_time = t_f - t

    # Find the time when the last visitor arrives
    last_visitor_time = visitors[-1]

    # Find the time when Vasya should arrive to be served immediately
    optimal_time = free_time

    # Iterate through the visitors and find the earliest time when Vasya can arrive to be served
    for visitor in visitors:
        if visitor <= free_time:
            optimal_time = visitor
            break

    return optimal_time

def main():
    t_s, t_f, t = map(int, input().split())
    n = int(input())
    visitors = list(map(int, input().split()))

    print(find_optimal_time(t_s, t_f, t, n, visitors))

if __name__ == '__main__':
    main()

