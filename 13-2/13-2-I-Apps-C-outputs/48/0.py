
def get_max_recordable_shows(n, k, shows):
    # Sort the shows by their start time
    shows.sort(key=lambda x: x[0])
    
    # Initialize the number of recordable shows to 0
    recordable_shows = 0
    
    # Iterate through the shows
    for i in range(n):
        # Check if the current show can be recorded
        if recordable_shows < k:
            # Increment the number of recordable shows
            recordable_shows += 1
        # Check if the current show ends before the next show starts
        elif shows[i][1] <= shows[i+1][0]:
            # Decrement the number of recordable shows
            recordable_shows -= 1
    
    # Return the maximum number of recordable shows
    return recordable_shows

def main():
    # Read the input
    n, k = map(int, input().split())
    shows = []
    for i in range(n):
        shows.append(list(map(int, input().split())))
    
    # Call the function to get the maximum number of recordable shows
    max_recordable_shows = get_max_recordable_shows(n, k, shows)
    
    # Print the output
    print(max_recordable_shows)

if __name__ == '__main__':
    main()

