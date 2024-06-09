
def get_criminals_info(cities, city_index, criminals):
    # Initialize a dictionary to store the information about the criminals
    criminals_info = {}
    
    # Iterate over the criminals
    for criminal in criminals:
        # Get the distance between the current criminal and the city where Limak lives
        distance = abs(criminal - city_index)
        
        # If the distance is not already in the dictionary, add it and set the number of criminals to 1
        if distance not in criminals_info:
            criminals_info[distance] = 1
        # If the distance is already in the dictionary, increment the number of criminals by 1
        else:
            criminals_info[distance] += 1
    
    return criminals_info

def catch_criminals(criminals_info):
    # Initialize a variable to store the number of criminals caught
    criminals_caught = 0
    
    # Iterate over the criminals_info dictionary
    for distance, num_criminals in criminals_info.items():
        # If the number of criminals at the current distance is 1, increment the number of criminals caught
        if num_criminals == 1:
            criminals_caught += 1
    
    return criminals_caught

def main():
    # Read the input
    n, a = map(int, input().split())
    t = list(map(int, input().split()))
    
    # Get the information about the criminals using the BCD
    criminals_info = get_criminals_info(n, a, t)
    
    # Catch the criminals
    criminals_caught = catch_criminals(criminals_info)
    
    # Print the number of criminals caught
    print(criminals_caught)

if __name__ == '__main__':
    main()

