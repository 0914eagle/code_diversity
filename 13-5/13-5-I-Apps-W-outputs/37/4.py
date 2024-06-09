
def get_network_coverage(n, a, b):
    # Initialize variables
    total_coverage = 0
    current_city = 1
    current_station = 1

    # Iterate through each city
    for i in range(n):
        # Calculate the coverage for the current city
        coverage = min(b[current_station - 1], a[current_city - 1])

        # Update the total coverage
        total_coverage += coverage

        # Update the current city and station
        current_city += 1
        if current_city > n:
            current_city = 1
        current_station += 1
        if current_station > n:
            current_station = 1

    # Check if the total coverage is greater than or equal to the total number of households
    if total_coverage >= sum(a):
        return "YES"
    else:
        return "NO"

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(get_network_coverage(n, a, b))

if __name__ == '__main__':
    main()

