
def get_maximum_media_companies(num_sectors, min_consecutive_sectors, min_distinct_colors, fan_assignments):
    # Initialize variables
    max_media_companies = 0
    current_media_companies = 0
    current_consecutive_sectors = 0
    current_distinct_colors = set()
    
    # Iterate through the fan assignments
    for i in range(num_sectors):
        # If the current sector is assigned to a team that is already in the current range, skip it
        if current_consecutive_sectors > 0 and fan_assignments[i] == fan_assignments[i - 1]:
            continue
        
        # If the current sector is assigned to a team that is not in the current range, start a new range
        if current_consecutive_sectors == 0 or fan_assignments[i] != fan_assignments[i - 1]:
            current_media_companies += 1
            current_consecutive_sectors = 1
            current_distinct_colors = set()
        
        # Add the color of the current team to the set of distinct colors
        current_distinct_colors.add(fan_assignments[i])
        
        # If the current range meets the minimum requirements, update the maximum number of media companies
        if current_consecutive_sectors >= min_consecutive_sectors and len(current_distinct_colors) >= min_distinct_colors:
            max_media_companies = max(max_media_companies, current_media_companies)
    
    # Return the maximum number of media companies
    return max_media_companies

def main():
    # Read the input
    num_sectors, min_consecutive_sectors, min_distinct_colors = map(int, input().split())
    fan_assignments = list(map(int, input().split()))
    
    # Solve the problem
    max_media_companies = get_maximum_media_companies(num_sectors, min_consecutive_sectors, min_distinct_colors, fan_assignments)
    
    # Print the output
    print(max_media_companies)

if __name__ == '__main__':
    main()

