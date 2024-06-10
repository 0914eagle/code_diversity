
def get_blue_balls(N, A, B):
    # Initialize a list to store the colors of the balls
    colors = []
    
    # Place A blue balls at the end of the list
    for i in range(A):
        colors.append("b")
    
    # Place B red balls at the end of the list
    for i in range(B):
        colors.append("r")
    
    # Return the number of blue balls among the first N balls
    return colors.count("b")

def main():
    # Read the input from stdin
    N, A, B = map(int, input().split())
    
    # Call the function to get the number of blue balls
    result = get_blue_balls(N, A, B)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

