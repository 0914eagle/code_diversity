
def get_tolls(tickets):
    # Initialize a dictionary to store the tolls for each exit
    tolls = {}
    # Iterate over the tickets
    for ticket in tickets:
        # Get the entrance and exit numbers from the ticket
        entrance, exit = ticket
        # If the exit has not been visited before, set its toll to 0
        if exit not in tolls:
            tolls[exit] = 0
        # If the entrance and exit are not the same, add the toll to the exit
        if entrance != exit:
            tolls[exit] += abs(entrance - exit)
    # Return the sum of the tolls for all exits
    return sum(tolls.values())

def get_min_tolls(tickets):
    # Initialize a set to store the visited exits
    visited = set()
    # Initialize a variable to store the minimum total tolls
    min_tolls = float('inf')
    # Iterate over the tickets
    for ticket in tickets:
        # Get the entrance and exit numbers from the ticket
        entrance, exit = ticket
        # If the exit has not been visited before, visit it and calculate the total tolls
        if exit not in visited:
            visited.add(exit)
            tolls = get_tolls(ticket)
            # If the total tolls are less than the minimum, update the minimum
            if tolls < min_tolls:
                min_tolls = tolls
    # Return the minimum total tolls
    return min_tolls

def main():
    # Read the number of trucks and their tickets
    num_trucks = int(input())
    tickets = []
    for _ in range(num_trucks):
        entrance, exit = map(int, input().split())
        tickets.append((entrance, exit))
    # Get the minimum total tolls
    min_tolls = get_min_tolls(tickets)
    # Print the minimum total tolls
    print(min_tolls)

if __name__ == '__main__':
    main()

