
def get_guard_post(n, guard_posts):
    # Initialize variables to keep track of the guard post with the lowest total cost
    min_cost = float('inf')
    min_guard_post = -1
    min_chocolate_cost = 0
    min_juice_cost = 0
    
    # Iterate through each guard post
    for i, guard_post in enumerate(guard_posts, start=1):
        # Unpack the guard post information
        chocolate_cost, juice_cost = guard_post
        
        # Calculate the total cost of buying one chocolate and one juice from this guard post
        total_cost = chocolate_cost + juice_cost
        
        # If the total cost is less than or equal to the given amount and less than the current minimum cost, update the minimum cost and guard post information
        if total_cost <= n and total_cost < min_cost:
            min_cost = total_cost
            min_guard_post = i
            min_chocolate_cost = chocolate_cost
            min_juice_cost = juice_cost
    
    # If a guard post with a total cost less than or equal to the given amount was found, return the guard post information
    if min_guard_post != -1:
        return min_guard_post, min_chocolate_cost, min_juice_cost
    
    # Otherwise, return -1
    return -1, 0, 0

