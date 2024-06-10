
def count_blue_balls(N, A, B):
    # Initialize a counter for the number of blue balls
    num_blue_balls = 0
    
    # Iterate through the first N balls
    for i in range(N):
        # If the current ball is blue, increment the counter
        if i % (A + B) < A:
            num_blue_balls += 1
    
    # Return the number of blue balls
    return num_blue_balls

def main():
    # Read the input from stdin
    N, A, B = map(int, input().split())
    
    # Call the count_blue_balls function and print the result
    print(count_blue_balls(N, A, B))

if __name__ == '__main__':
    main()

