
def find_optimal_time(t_start, t_end, t_visit, visitors):
    # Find the earliest time that Vasya can arrive to be served
    earliest_time = max(visitors)

    # Find the latest time that Vasya can arrive to be served
    latest_time = t_end - t_visit

    # Initialize the optimal time to be the earliest time
    optimal_time = earliest_time

    # Iterate through each visitor and check if Vasya can arrive at a later time to be served
    for visitor in visitors:
        if visitor + t_visit <= latest_time:
            optimal_time = visitor + t_visit

    return optimal_time

def main():
    t_start, t_end, t_visit = map(int, input().split())
    n = int(input())
    visitors = [int(x) for x in input().split()]

    print(find_optimal_time(t_start, t_end, t_visit, visitors))

if __name__ == '__main__':
    main()

