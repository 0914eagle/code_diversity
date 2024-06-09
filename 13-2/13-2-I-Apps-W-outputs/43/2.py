
def solve(n, x, y, c, k):
    # Initialize the minimum cost to infinity
    min_cost = float('inf')
    # Initialize the optimal solution
    opt_sol = []
    
    # Loop through all possible combinations of power stations and connections
    for ps in range(1, 2**n):
        # Convert the binary string to a list of cities with power stations
        ps_cities = [i for i in range(n) if ps & (1 << i)]
        # Calculate the cost of building power stations in these cities
        ps_cost = sum(c[i] for i in ps_cities)
        # Initialize the cost of connections to 0
        conn_cost = 0
        # Loop through all possible connections
        for i in range(n):
            for j in range(i+1, n):
                # Check if the connection is valid
                if x[i] == x[j] or y[i] == y[j]:
                    # Calculate the cost of the connection
                    conn_cost += k[i] + k[j]
        # Calculate the total cost
        total_cost = ps_cost + conn_cost
        # Check if the total cost is less than the minimum cost
        if total_cost < min_cost:
            # Update the minimum cost and the optimal solution
            min_cost = total_cost
            opt_sol = [ps_cities, conn_cost]
    
    # Return the optimal solution
    return [min_cost, opt_sol[0], opt_sol[1]]

