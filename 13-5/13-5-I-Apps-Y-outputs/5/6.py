
def f1(N, values):
    # Initialize the maximum value of the last ingredient as 0
    max_value = 0
    
    # Loop through each combination of ingredients
    for i in range(N):
        for j in range(i+1, N):
            # Calculate the value of the new ingredient
            new_value = (values[i] + values[j]) / 2
            
            # Update the maximum value if necessary
            if new_value > max_value:
                max_value = new_value
    
    # Return the maximum value
    return max_value

def f2(N, values):
    # Initialize the maximum value of the last ingredient as 0
    max_value = 0
    
    # Loop through each combination of ingredients
    for i in range(N):
        for j in range(i+1, N):
            # Calculate the value of the new ingredient
            new_value = (values[i] + values[j]) / 2
            
            # Update the maximum value if necessary
            if new_value > max_value:
                max_value = new_value
    
    # Return the maximum value
    return max_value

if __name__ == '__main__':
    N = int(input())
    values = list(map(int, input().split()))
    print(f1(N, values))
    print(f2(N, values))

