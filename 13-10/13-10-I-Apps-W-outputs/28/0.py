
def get_min_days_to_collect_all_pebbles(n_types, k_per_pocket, pebbles_per_type):
    # Initialize variables
    total_pebbles = 0
    days = 0
    pockets = [0] * n_types

    # Loop through each type of pebble
    for i in range(n_types):
        # Calculate the number of pebbles of this type that Anastasia can collect on this day
        day_pebbles = min(pebbles_per_type[i], k_per_pocket - pockets[i])

        # Add the number of pebbles of this type to the total
        total_pebbles += day_pebbles

        # Update the number of pebbles in each pocket
        pockets[i] += day_pebbles

        # If Anastasia has collected all the pebbles of this type, move on to the next type
        if pockets[i] == pebbles_per_type[i]:
            continue

        # If Anastasia has collected all the pebbles, break out of the loop
        if total_pebbles == sum(pebbles_per_type):
            break

        # Otherwise, increase the number of days by 1
        days += 1

    # Return the minimum number of days needed to collect all the pebbles
    return days

def main():
    n_types, k_per_pocket = map(int, input().split())
    pebbles_per_type = list(map(int, input().split()))
    print(get_min_days_to_collect_all_pebbles(n_types, k_per_pocket, pebbles_per_type))

if __name__ == '__main__':
    main()

