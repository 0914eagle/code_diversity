
def get_criminals(n, a, t):
    # Initialize a list to store the criminals
    criminals = []
    
    # Iterate through the input array
    for i in range(n):
        # If there is a criminal in the current city
        if t[i] == 1:
            # Add the city to the list of criminals
            criminals.append(i)
    
    # Return the list of criminals
    return criminals

def get_criminals_caught(n, a, t):
    # Get the list of criminals
    criminals = get_criminals(n, a, t)
    
    # Initialize a variable to store the number of criminals caught
    criminals_caught = 0
    
    # Iterate through the list of criminals
    for criminal in criminals:
        # If the criminal is not in the current city
        if criminal != a:
            # Increment the number of criminals caught
            criminals_caught += 1
    
    # Return the number of criminals caught
    return criminals_caught

if __name__ == '__main__':
    n, a = map(int, input().split())
    t = list(map(int, input().split()))
    print(get_criminals_caught(n, a, t))

