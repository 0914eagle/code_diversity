
def get_min_x_value(a, d, b):
    # Initialize variables
    x_1 = 0
    x_2 = 0
    n = len(a)
    
    # Iterate through each room
    for i in range(n):
        # Get the number of students in the room
        num_students = a[i]
        
        # Check if the number of students is different from the official number
        if num_students != b:
            # Check which instructor processed the room
            if i % 2 == 0:
                x_1 += 1
            else:
                x_2 += 1
    
    # Return the minimum value of x_1 and x_2
    return min(x_1, x_2)

def main():
    # Read the input
    n, d, b = map(int, input().split())
    a = list(map(int, input().split()))
    
    # Call the get_min_x_value function
    min_x_value = get_min_x_value(a, d, b)
    
    # Print the result
    print(min_x_value)

if __name__ == '__main__':
    main()

