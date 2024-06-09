
def possible_stop_heights(up_days, down_days):
    N = up_days + down_days + 1
    stops = []
    
    for i in range(up_days + 1):
        stops.append(N - i)
    
    for i in range(1, down_days + 1):
        stops.insert(i, i)
    
    return stops

# Read input
up_days = int(input())
down_days = int(input())

# Get possible stop heights
possible_stops = possible_stop_heights(up_days, down_days)

# Print the possible stop heights
print(*possible_stops)
