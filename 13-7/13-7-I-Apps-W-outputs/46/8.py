
def get_earliest_time_to_arrive(n, m, t_a, t_b, k, a_list, b_list):
    # Sort the lists of flight times
    a_list.sort()
    b_list.sort()
    
    # Initialize the variables
    earliest_time = -1
    flights_cancelled = 0
    
    # Iterate through the flights from A to B
    for i in range(n):
        # Check if the flight is not cancelled and if it is possible to take the flight and the next flight from B to C
        if flights_cancelled < k and a_list[i] + t_a <= b_list[0]:
            # Cancel the flight and update the variables
            flights_cancelled += 1
            earliest_time = a_list[i] + t_a + b_list[0]
        # Check if the flight is not cancelled and if it is possible to take the flight and the next flight from B to C
        elif flights_cancelled < k and a_list[i] + t_a > b_list[0]:
            # Cancel the flight and update the variables
            flights_cancelled += 1
            earliest_time = a_list[i] + t_a + b_list[1]
    
    # Check if it is possible to cancel k or less flights and still reach C
    if flights_cancelled <= k:
        return earliest_time
    else:
        return -1

def main():
    n, m, t_a, t_b, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    print(get_earliest_time_to_arrive(n, m, t_a, t_b, k, a_list, b_list))

if __name__ == '__main__':
    main()

