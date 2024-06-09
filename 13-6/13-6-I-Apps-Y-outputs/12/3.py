
def solve(parts, days):
    # Initialize a set to store the unique parts
    unique_parts = set()
    # Loop through each day
    for day in range(1, days+1):
        # If the part for the current day is not in the set, add it
        if parts[day-1] not in unique_parts:
            unique_parts.add(parts[day-1])
        # If the number of unique parts is equal to the total number of parts, return the current day
        if len(unique_parts) == parts:
            return day
    # If all parts have been replaced, return "paradox avoided"
    return "paradox avoided"

