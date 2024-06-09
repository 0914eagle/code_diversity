
def solve(precincts, districts):
    # Initialize variables to keep track of votes and wasted votes
    votes_a, votes_b = 0, 0
    wasted_a, wasted_b = 0, 0
    
    # Iterate through each precinct
    for precinct in precincts:
        # Get the district and party votes for the precinct
        district, votes_a_precinct, votes_b_precinct = precinct
        
        # Add the party votes for the precinct to the total votes
        votes_a += votes_a_precinct
        votes_b += votes_b_precinct
        
        # Check if the party with more votes wins the district
        if votes_a_precinct > votes_b_precinct:
            # Add the wasted votes for the losing party
            wasted_b += votes_b_precinct
        else:
            wasted_a += votes_a_precinct
    
    # Calculate the efficiency gap
    efficiency_gap = abs(wasted_a - wasted_b) / (votes_a + votes_b)
    
    # Return the winner, wasted votes, and efficiency gap for each district
    return [(wasted_a > wasted_b) * "A" + (wasted_a <= wasted_b) * "B", wasted_a, wasted_b], efficiency_gap

