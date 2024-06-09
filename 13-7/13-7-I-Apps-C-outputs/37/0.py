
def solve(gigs, venues, roads, travel_time):
    # Initialize a graph to store the connections between venues
    graph = {}
    for i in range(venues):
        graph[i] = []
    
    # Add edges to the graph based on the roads
    for i in range(roads):
        start, end, time = roads[i]
        graph[start].append((end, time))
        graph[end].append((start, time))
    
    # Initialize a dictionary to store the gig offers
    gigs_dict = {}
    for i in range(gigs):
        venue, start, end, money = gigs[i]
        gigs_dict[venue] = (start, end, money)
    
    # Initialize a variable to store the maximum amount of money that can be made
    max_money = 0
    
    # Iterate over all possible combinations of gigs
    for i in range(1 << gigs):
        # Initialize a variable to store the current amount of money
        current_money = 0
        
        # Iterate over all gigs that are selected in the current combination
        for j in range(gigs):
            # If the j-th gig is selected, add its money to the current amount of money
            if (i >> j) & 1:
                current_money += gigs_dict[j + 1][2]
        
        # If the current amount of money is greater than the maximum amount of money, update the maximum amount of money
        if current_money > max_money:
            max_money = current_money
    
    return max_money

