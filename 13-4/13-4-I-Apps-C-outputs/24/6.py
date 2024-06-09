
def get_max_tastiness(n, k, a, b, tastiness, complementary_pairs):
    # Initialize the maximum tastiness and cost
    max_tastiness = 0
    max_cost = 0
    
    # Loop through each possible combination of scoops
    for num_scoops in range(1, n + 1):
        for scoop_order in itertools.permutations(range(k), num_scoops):
            # Calculate the tastiness and cost of this combination
            tastiness_sum = 0
            cost_sum = 0
            for i in range(num_scoops):
                tastiness_sum += tastiness[scoop_order[i]]
                cost_sum += a
            for i in range(num_scoops - 1):
                for j in range(i + 1, num_scoops):
                    if (scoop_order[i], scoop_order[j]) in complementary_pairs:
                        tastiness_sum += complementary_pairs[(scoop_order[i], scoop_order[j])]
            cost_sum += b
            
            # Update the maximum tastiness and cost if necessary
            if tastiness_sum > max_tastiness:
                max_tastiness = tastiness_sum
                max_cost = cost_sum
    
    # Return the maximum tastiness per gold coin ratio
    if max_cost == 0:
        return 0
    else:
        return max_tastiness / max_cost

