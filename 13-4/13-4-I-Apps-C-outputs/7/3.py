
def solve(N, D, buildings):
    # Initialize the covered segment as the entire city
    covered_segment = [0, D]
    
    # Iterate through the buildings and update the covered segment
    for building in buildings:
        # If the building has a transmitter, update the covered segment
        if building[0] == 1:
            covered_segment[0] = max(covered_segment[0], building[1])
            covered_segment[1] = min(covered_segment[1], building[1] + building[2])
    
    # Return the length of the covered segment
    return covered_segment[1] - covered_segment[0]

