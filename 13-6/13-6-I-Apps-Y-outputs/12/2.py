
def solve(parts, days):
    # Initialize a set to store the unique parts
    unique_parts = set()
    # Iterate through the days
    for i in range(days):
        # If the current part is not in the set, add it to the set
        if parts[i] not in unique_parts:
            unique_parts.add(parts[i])
        # If the set size is equal to the number of parts, return the current day
        if len(unique_parts) == parts:
            return i
    # If the set size is not equal to the number of parts at the end of the days, return "paradox avoided"
    return "paradox avoided"

