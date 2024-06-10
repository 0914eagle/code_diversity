
def get_min_time(a, b, c):
    
    # Sort the sticks in descending order
    sticks = sorted([a, b, c], reverse=True)

    # Initialize the minimum time needed to assemble the triangle
    min_time = 0

    # Loop through the sticks and calculate the minimum time needed to assemble the triangle
    for i in range(len(sticks)):
        # Calculate the length of the current stick
        current_length = sticks[i]

        # Calculate the length of the other two sticks
        other_length_1 = sticks[(i + 1) % 3]
        other_length_2 = sticks[(i + 2) % 3]

        # Calculate the minimum length needed to form a triangle
        min_length = max(other_length_1, other_length_2)

        # Calculate the difference between the current length and the minimum length
        diff = current_length - min_length

        # If the difference is positive, calculate the minimum time needed to increase the current length
        if diff > 0:
            min_time += diff

    return min_time

def main():
    a, b, c = map(int, input().split())
    print(get_min_time(a, b, c))

if __name__ == '__main__':
    main()

