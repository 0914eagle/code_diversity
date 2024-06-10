
def get_min_max_x(n, d, b, a):
    # Initialize variables
    x_1 = 0
    x_2 = 0
    rooms_processed = 0
    students_hidden = 0
    
    # Iterate through each room
    for i in range(n):
        # Check if the room is processed by the first instructor
        if i % 2 == 1:
            # Check if the room has more or less students than expected
            if a[i] != b:
                # Update the number of rooms with non-hidden students
                x_1 += 1
            # Update the number of processed rooms
            rooms_processed += 1
        
        # Check if the room is processed by the second instructor
        if i % 2 == 0:
            # Check if the room has more or less students than expected
            if a[i] != b:
                # Update the number of rooms with non-hidden students
                x_2 += 1
            # Update the number of processed rooms
            rooms_processed += 1
        
        # Check if all rooms are processed
        if rooms_processed == n:
            # Break the loop
            break
    
    # Return the minimum of x_1 and x_2
    return min(x_1, x_2)

def main():
    # Read the input
    n, d, b = map(int, input().split())
    a = list(map(int, input().split()))
    
    # Call the get_min_max_x function
    min_max_x = get_min_max_x(n, d, b, a)
    
    # Print the result
    print(min_max_x)

if __name__ == '__main__':
    main()

