
def get_guard_post(n, guard_posts):
    # Initialize variables to keep track of the minimum cost and the guard post with the minimum cost
    min_cost = float('inf')
    min_cost_guard_post = None
    
    # Iterate through the guard posts
    for guard_post in guard_posts:
        # Initialize variables to keep track of the total cost and the number of gifts bought
        total_cost = 0
        num_gifts = 0
        
        # Iterate through the guards in the current guard post
        for guard in guard_post:
            # Check if the current guard can be bribed with the remaining money
            if total_cost + guard[0] <= n:
                # Add the cost of the current guard to the total cost
                total_cost += guard[0]
                # Increment the number of gifts bought
                num_gifts += 1
        
        # Check if the total cost is less than the minimum cost and the number of gifts bought is equal to the number of guards in the guard post
        if total_cost < min_cost and num_gifts == len(guard_post):
            # Update the minimum cost and the guard post with the minimum cost
            min_cost = total_cost
            min_cost_guard_post = guard_post
    
    # Check if a guard post with the minimum cost has been found
    if min_cost_guard_post is not None:
        # Return the guard post number and the cost of the gifts
        return [guard_posts.index(min_cost_guard_post) + 1, min_cost_guard_post[0][0], min_cost_guard_post[1][0]]
    else:
        # Return -1 if no guard post with the minimum cost has been found
        return [-1, -1, -1]

