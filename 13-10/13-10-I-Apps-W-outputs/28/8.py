
def get_days_needed(n_types, max_pocket_size, pebble_counts):
    # Initialize variables
    days_needed = 0
    total_pebbles = sum(pebble_counts)
    current_pocket_size = 0
    current_pebbles = 0

    # Iterate through the pebble types
    for i in range(n_types):
        # Calculate the number of pebbles that can be collected on this day
        pebbles_to_collect = min(pebble_counts[i], max_pocket_size - current_pocket_size)

        # Update the total number of pebbles collected and the current pocket size
        current_pocket_size += pebbles_to_collect
        current_pebbles += pebbles_to_collect

        # Check if all pebbles have been collected
        if current_pebbles == total_pebbles:
            break

        # Increment the number of days needed
        days_needed += 1

        # Reset the current pocket size if it exceeds the maximum size
        if current_pocket_size > max_pocket_size:
            current_pocket_size = 0

    return days_needed

def main():
    n_types, max_pocket_size = map(int, input().split())
    pebble_counts = list(map(int, input().split()))
    print(get_days_needed(n_types, max_pocket_size, pebble_counts))

if __name__ == '__main__':
    main()

