
def find_shortest_cycle(numbers):
    # Initialize a set to store the visited nodes
    visited = set()
    # Initialize a list to store the cycle
    cycle = []
    # Iterate through the numbers
    for num in numbers:
        # If the number is not in the visited set, add it to the visited set and the cycle list
        if num not in visited:
            visited.add(num)
            cycle.append(num)
        # If the number is in the visited set, it means we have found a cycle
        else:
            # Return the length of the cycle
            return len(cycle) - visited.index(num)
    # If we reach the end of the numbers and there is no cycle, return -1
    return -1

