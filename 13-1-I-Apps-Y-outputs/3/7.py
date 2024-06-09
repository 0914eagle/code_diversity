
def solve(precincts, districts):
    # Initialize variables to keep track of the votes and wasted votes
    votes_a, votes_b = 0, 0
    wasted_a, wasted_b = 0, 0
    
    # Iterate through each precinct
    for precinct in precincts:
        # Get the district and party votes for the precinct
        district, votes_a_precinct, votes_b_precinct = precinct
        
        # Add the party votes for the precinct to the total votes
        votes_a += votes_a_precinct
        votes_b += votes_b_precinct
        
        # Check if the party A or B wins the precinct
        if votes_a_precinct > votes_b_precinct:
            # If party A wins, add the wasted votes for party B
            wasted_b += votes_b_precinct
        else:
            # If party B wins, add the wasted votes for party A
            wasted_a += votes_a_precinct
    
    # Iterate through each district
    for district in range(1, districts + 1):
        # Get the party that wins the district
        if votes_a > votes_b:
            party = "A"
        else:
            party = "B"
        print(party)
    
    # Print the wasted votes for each party
    print(wasted_a, wasted_b)
    
    # Calculate the efficiency gap
    efficiency_gap = abs(wasted_a - wasted_b) / (votes_a + votes_b)
    print(efficiency_gap)

