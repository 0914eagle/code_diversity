
def count_ways(trenches):
    # Initialize a set to store the endpoints of the trenches
    endpoints = set()
    # Loop through each trench and add its endpoints to the set
    for trench in trenches:
        endpoints.add((trench[0], trench[1]))
        endpoints.add((trench[2], trench[3]))
    
    # Initialize a dictionary to store the number of ways for each endpoint
    ways = {}
    # Loop through each endpoint and count the number of ways it can be watched
    for endpoint in endpoints:
        ways[endpoint] = 0
        for trench in trenches:
            if endpoint in trench:
                ways[endpoint] += 1
    
    # Return the number of endpoints with at least two ways
    return sum(1 for way in ways.values() if way >= 2)

