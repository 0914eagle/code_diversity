
def get_minimum_bags(n, k, a):
    # Initialize variables
    bags = 0
    current_bag = 0
    current_day = 0

    # Iterate through the input array
    for i in range(n):
        # If the current day's garbage is less than or equal to the bag's capacity, add it to the current bag
        if a[i] <= k:
            current_bag += a[i]
        # If the current day's garbage is greater than the bag's capacity, start a new bag
        else:
            bags += 1
            current_bag = a[i]

    # Add the last bag if it's not empty
    if current_bag > 0:
        bags += 1

    return bags

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_minimum_bags(n, k, a))

