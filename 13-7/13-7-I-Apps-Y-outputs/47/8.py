
def get_blue_balls(N, A, B):
    # Initialize a list to store the colors of the balls
    colors = []
    
    # Place A blue balls at the end of the row
    for i in range(A):
        colors.append("b")
    
    # Place B red balls at the end of the row
    for i in range(B):
        colors.append("r")
    
    # Count the number of blue balls among the first N balls
    return colors.count("b")

def main():
    # Read the input from stdin
    N, A, B = map(int, input().split())
    
    # Call the function to get the number of blue balls
    num_blue_balls = get_blue_balls(N, A, B)
    
    # Print the result
    print(num_blue_balls)

if __name__ == '__main__':
    main()

