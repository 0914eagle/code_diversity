
def get_min_chairs(n, left_right_requirements):
    # Initialize variables
    min_chairs = 0
    current_chair = 1
    total_chairs = 0
    guests = []

    # Iterate through the left and right requirements for each guest
    for left, right in left_right_requirements:
        # If the current chair is not occupied, assign it to the guest
        if current_chair not in guests:
            guests.append(current_chair)
            current_chair += 1

        # If the current chair is occupied, move to the next chair
        else:
            current_chair += 1

        # Add the left and right requirements to the total number of chairs
        total_chairs += left + right

    # Return the minimum number of chairs required
    return total_chairs

def main():
    # Read the number of guests and their left and right requirements
    n = int(input())
    left_right_requirements = []
    for _ in range(n):
        left, right = map(int, input().split())
        left_right_requirements.append((left, right))

    # Call the get_min_chairs function and print the result
    print(get_min_chairs(n, left_right_requirements))

if __name__ == '__main__':
    main()

