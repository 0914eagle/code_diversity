
def solve(parts, days):
    # Initialize a set to store the unique parts
    unique_parts = set()
    # Iterate through the list of parts
    for part in parts:
        # If the part is not in the set, add it to the set
        if part not in unique_parts:
            unique_parts.add(part)
        # If the set size is equal to the number of parts, return the current day
        if len(unique_parts) == len(parts):
            return days
    # If the set size is not equal to the number of parts, return "paradox avoided"
    return "paradox avoided"

