
def get_min_max_occupied_houses(n, x):
    # Initialize variables
    min_occupied_houses = 0
    max_occupied_houses = 0
    
    # Loop through each friend and calculate the number of occupied houses
    for i in range(n):
        # Calculate the number of occupied houses for the current friend
        num_occupied_houses = 0
        for j in range(n):
            if x[j] == x[i] or x[j] == x[i] - 1 or x[j] == x[i] + 1:
                num_occupied_houses += 1
        
        # Update the minimum and maximum number of occupied houses
        min_occupied_houses = min(min_occupied_houses, num_occupied_houses)
        max_occupied_houses = max(max_occupied_houses, num_occupied_houses)
    
    return min_occupied_houses, max_occupied_houses

def main():
    n = int(input())
    x = list(map(int, input().split()))
    min_occupied_houses, max_occupied_houses = get_min_max_occupied_houses(n, x)
    print(min_occupied_houses, max_occupied_houses)

if __name__ == '__main__':
    main()

