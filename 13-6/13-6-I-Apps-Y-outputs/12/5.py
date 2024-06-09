
def solve(parts, days):
    # Initialize a set to store the unique parts
    unique_parts = set()
    # Iterate through each day
    for i in range(days):
        # If the current part is not in the unique parts set, add it
        if parts[i] not in unique_parts:
            unique_parts.add(parts[i])
        # If the number of unique parts is equal to the total number of parts, return the current day
        if len(unique_parts) == parts:
            return i
    # If all the parts have been replaced, return "paradox avoided"
    return "paradox avoided"

