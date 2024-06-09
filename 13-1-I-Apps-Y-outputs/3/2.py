
def solve(precincts, districts):
    # Initialize variables to keep track of the number of wasted votes and the efficiency gap
    wasted_votes_A, wasted_votes_B = 0, 0
    efficiency_gap = 0

    # Iterate through each precinct
    for precinct in precincts:
        # Get the district and party vote totals for the precinct
        district, a_votes, b_votes = precinct

        # Calculate the number of wasted votes for each party
        wasted_votes_A += max(0, a_votes - (b_votes + 1) // 2)
        wasted_votes_B += max(0, b_votes - (a_votes + 1) // 2)

    # Calculate the efficiency gap
    efficiency_gap = abs(wasted_votes_A - wasted_votes_B) / sum(a_votes + b_votes for precinct in precincts)

    # Return the winner, wasted votes, and efficiency gap for each district
    return [(district, "A" if a_votes > b_votes else "B", wasted_votes_A, wasted_votes_B) for district, a_votes, b_votes in precincts], efficiency_gap

