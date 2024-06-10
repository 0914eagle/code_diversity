
def get_rating(r, n):
    # Calculate the sum of the ratings
    sum_r = sum(r)
    
    # Calculate the average rating
    avg_r = sum_r / n
    
    # Calculate the difference between the average rating and each individual rating
    diff = [abs(avg_r - ri) for ri in r]
    
    # Return the rating that is closest to the average rating
    return r[diff.index(min(diff))]

def get_matches(r, n):
    # Initialize variables
    matches = []
    match_count = 0
    
    # While there are still friends with different ratings
    while len(set(r)) > 1:
        # Get the rating that is closest to the average rating
        avg_r = get_rating(r, n)
        
        # Create a match with all friends with a rating different from the average rating
        match = [i for i, ri in enumerate(r) if ri != avg_r]
        
        # Add the match to the list of matches
        matches.append(match)
        
        # Update the ratings of the friends in the match
        for i in match:
            r[i] = avg_r
        
        # Increment the match count
        match_count += 1
    
    # Return the list of matches
    return matches

def get_output(r, n):
    # Get the list of matches
    matches = get_matches(r, n)
    
    # Initialize the output variables
    output_r = [0] * n
    output_t = len(matches)
    output_matches = []
    
    # Loop through the matches
    for match in matches:
        # Initialize the match output
        match_output = ['0'] * n
        
        # Loop through the friends in the match
        for i in match:
            # Set the match output for the friend to '1'
            match_output[i] = '1'
        
        # Add the match output to the list of match outputs
        output_matches.append(''.join(match_output))
    
    # Return the output variables
    return output_r, output_t, output_matches

if __name__ == '__main__':
    # Read the input
    n = int(input())
    r = list(map(int, input().split()))
    
    # Get the output
    output_r, output_t, output_matches = get_output(r, n)
    
    # Print the output
    print(*output_r)
    print(output_t)
    for match in output_matches:
        print(match)

