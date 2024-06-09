
def f1(N, colors):
    # Initialize the number of operations to 0
    operations = 0
    
    # Loop through the colors from left to right
    for i in range(N):
        # If the current color is white and the next color is red, swap them
        if colors[i] == "W" and colors[i+1] == "R":
            operations += 1
            colors[i], colors[i+1] = colors[i+1], colors[i]
    
    # Return the number of operations needed
    return operations

def f2(N, colors):
    # Initialize the number of operations to 0
    operations = 0
    
    # Loop through the colors from left to right
    for i in range(N):
        # If the current color is white and the previous color is red, change the color to red
        if colors[i] == "W" and colors[i-1] == "R":
            operations += 1
            colors[i] = "R"
    
    # Return the number of operations needed
    return operations

if __name__ == '__main__':
    N = int(input())
    colors = input()
    print(min(f1(N, colors), f2(N, colors)))

