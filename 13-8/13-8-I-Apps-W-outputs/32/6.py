
def get_comfort(people, cities):
    # Initialize comfort as 0
    comfort = 0
    
    # Iterate over the people and calculate the comfort for each segment
    for i in range(len(people)):
        # Get the city code for the current person
        city = cities[i]
        
        # Find the next person who is going to the same city
        j = i + 1
        while j < len(people) and cities[j] != city:
            j += 1
        
        # If there is a person who is going to the same city, calculate the comfort for the segment
        if j < len(people):
            comfort += city ^ cities[j]
    
    # Return the total comfort
    return comfort

def main():
    # Read the number of people and their city codes
    n = int(input())
    cities = [int(x) for x in input().split()]
    
    # Call the get_comfort function to get the maximum comfort
    comfort = get_comfort(range(n), cities)
    
    # Print the result
    print(comfort)

if __name__ == '__main__':
    main()

