
def solve(parts, days):
    # Initialize a set to store the unique parts
    unique_parts = set()
    # Loop through each day
    for i in range(len(days)):
        # If the part on this day is not in the set, add it
        if days[i] not in unique_parts:
            unique_parts.add(days[i])
        # If the set size is equal to the number of parts, return the current day
        if len(unique_parts) == parts:
            return i
    # If all parts are not replaced, return "paradox avoided"
    return "paradox avoided"

