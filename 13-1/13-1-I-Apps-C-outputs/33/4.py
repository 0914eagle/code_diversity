
def get_minimum_bags(n, k, a):
    # Initialize variables
    bags = 0
    current_bag = 0
    day = 1

    # Iterate through the input array
    for i in range(n):
        # If the current day's garbage is less than or equal to the bag's capacity, add it to the current bag
        if a[i] <= k:
            current_bag += a[i]
        # If the current day's garbage is greater than the bag's capacity, create a new bag and add the remaining garbage to it
        else:
            bags += 1
            current_bag = a[i] - k

        # If it's the last day, add the current bag to the total number of bags
        if day == n:
            bags += 1

        # Increment the day
        day += 1

    return bags

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_minimum_bags(n, k, a))

