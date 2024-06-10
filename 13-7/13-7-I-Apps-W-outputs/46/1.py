
def get_optimal_time(n, m, t_a, t_b, k, a_times, b_times):
    # Sort the flight times from A to B and from B to C in increasing order
    a_times.sort()
    b_times.sort()
    
    # Initialize the optimal time as the latest possible time
    optimal_time = b_times[-1]
    
    # Iterate through the flights from A to B
    for i in range(n):
        # Find the corresponding flight from B to C that departs after the flight from A to B arrives
        j = binary_search(b_times, a_times[i] + t_a)
        if j != -1:
            # Calculate the time when Arkady arrives at C if he takes the current flight from A to B and the flight from B to C
            time = a_times[i] + t_a + b_times[j] - t_b
            # Update the optimal time if necessary
            optimal_time = min(optimal_time, time)
    
    return optimal_time

def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= x:
            right = mid - 1
        else:
            left = mid + 1
    if left < len(arr) and arr[left] == x:
        return left
    else:
        return -1

if __name__ == '__main__':
    n, m, t_a, t_b, k = map(int, input().split())
    a_times = list(map(int, input().split()))
    b_times = list(map(int, input().split()))
    print(get_optimal_time(n, m, t_a, t_b, k, a_times, b_times))

