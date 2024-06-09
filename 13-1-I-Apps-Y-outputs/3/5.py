
def get_wasted_votes(precincts, party):
    wasted_votes = 0
    for precinct in precincts:
        if precinct[party] == 0:
            continue
        votes_needed = (precinct[0] * 100) // 2 + 1 - precinct[party]
        if votes_needed > 0:
            wasted_votes += votes_needed
    return wasted_votes

def get_efficiency_gap(precincts):
    party_a_votes = 0
    party_b_votes = 0
    for precinct in precincts:
        party_a_votes += precinct[1]
        party_b_votes += precinct[2]
    total_votes = party_a_votes + party_b_votes
    efficiency_gap = abs(party_a_votes - party_b_votes) / total_votes
    return efficiency_gap

def solve(precincts):
    party_a_wasted_votes = get_wasted_votes(precincts, 1)
    party_b_wasted_votes = get_wasted_votes(precincts, 2)
    efficiency_gap = get_efficiency_gap(precincts)
    return party_a_wasted_votes, party_b_wasted_votes, efficiency_gap

