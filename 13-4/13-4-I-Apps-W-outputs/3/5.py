
def get_guardpost(n, guardposts):
    # Initialize variables to keep track of the minimum cost and the guardpost number
    min_cost = float('inf')
    guardpost_number = -1
    
    # Iterate through the guardposts
    for i, guardpost in enumerate(guardposts, start=1):
        # Get the minimum cost for each guardpost
        cost = get_min_cost(n, guardpost)
        
        # If the cost is less than the minimum cost, update the minimum cost and the guardpost number
        if cost < min_cost:
            min_cost = cost
            guardpost_number = i
    
    # Return the guardpost number and the minimum cost for each guard
    return guardpost_number, min_cost, min_cost

def get_min_cost(n, guardpost):
    # Unpack the guardpost
    chocolate_min, juice_min = guardpost
    
    # Initialize variables to keep track of the minimum cost
    min_cost = float('inf')
    
    # Iterate through the possible chocolate prices
    for chocolate in range(1, n+1):
        # If the chocolate price is less than the minimum chocolate price, continue to the next iteration
        if chocolate < chocolate_min:
            continue
        
        # Iterate through the possible juice prices
        for juice in range(1, n+1):
            # If the juice price is less than the minimum juice price, continue to the next iteration
            if juice < juice_min:
                continue
            
            # Calculate the total cost
            total_cost = chocolate + juice
            
            # If the total cost is less than the minimum cost, update the minimum cost
            if total_cost < min_cost:
                min_cost = total_cost
    
    # Return the minimum cost
    return min_cost

guardposts = [(5, 6), (6, 7), (5, 6), (9, 9)]
n = 10

guardpost_number, chocolate_cost, juice_cost = get_guardpost(n, guardposts)

print(guardpost_number, chocolate_cost, juice_cost)

