
def get_comfort(people, cities):
    # Initialize comfort as 0
    comfort = 0
    
    # Iterate through the people and calculate the comfort for each segment
    for i in range(len(people)):
        # Get the city code for the current person
        city = cities[i]
        
        # Get the city codes for the people in the same segment as the current person
        segment_cities = [cities[j] for j in range(i, len(people)) if people[j] == people[i]]
        
        # Calculate the XOR of the city codes for the current segment
        segment_comfort = city ^ sum(segment_cities)
        
        # Add the segment comfort to the total comfort
        comfort += segment_comfort
    
    # Return the total comfort
    return comfort

def main():
    # Read the number of people and their city codes from stdin
    n = int(input())
    people = list(map(int, input().split()))
    cities = list(map(int, input().split()))
    
    # Call the get_comfort function to get the maximum possible comfort
    comfort = get_comfort(people, cities)
    
    # Print the result
    print(comfort)

if __name__ == '__main__':
    main()

