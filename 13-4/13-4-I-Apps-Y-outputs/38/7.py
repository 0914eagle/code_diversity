
def get_max_d(n, x, x_list):
    # Sort the list of city coordinates in ascending order
    x_list.sort()
    
    # Initialize the maximum value of D
    max_d = 0
    
    # Iterate through the list of city coordinates
    for i in range(n):
        # Calculate the distance between the current city and the previous city
        dist = x_list[i] - x
        
        # If the distance is greater than the maximum value of D, update the maximum value of D
        if dist > max_d:
            max_d = dist
    
    return max_d

def main():
    # Read the input data
    n, x = map(int, input().split())
    x_list = list(map(int, input().split()))
    
    # Calculate the maximum value of D
    max_d = get_max_d(n, x, x_list)
    
    # Print the result
    print(max_d)

if __name__ == '__main__':
    main()

