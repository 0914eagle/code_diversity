
def get_optimal_time(n, m, t_a, t_b, k, a_list, b_list):
    # Sort the lists of departure times
    a_list.sort()
    b_list.sort()
    # Initialize the optimal time to be the latest possible time
    optimal_time = 10**9 + 1
    # Loop through all possible combinations of flights to cancel
    for i in range(k+1):
        # Initialize the current time to be the earliest possible time
        current_time = 0
        # Loop through the flights from A to B
        for j in range(n):
            # If the current flight is not cancelled, add its departure time to the current time
            if j not in range(i):
                current_time += a_list[j]
        # Loop through the flights from B to C
        for j in range(m):
            # If the current flight is not cancelled and its departure time is greater than or equal to the current time, add its departure time to the current time
            if j not in range(i) and b_list[j] >= current_time + t_a:
                current_time = b_list[j]
        # If the current time is less than the optimal time, update the optimal time
        if current_time < optimal_time:
            optimal_time = current_time
    # If no flights can be cancelled, return -1
    if optimal_time == 10**9 + 1:
        return -1
    # Otherwise, return the optimal time
    return optimal_time

def main():
    n, m, t_a, t_b, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    print(get_optimal_time(n, m, t_a, t_b, k, a_list, b_list))

if __name__ == '__main__':
    main()

