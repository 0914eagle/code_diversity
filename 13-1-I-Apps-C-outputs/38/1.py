
def solve(records):
    # Initialize a set to store the unique visitors
    visitors = set()

    # Iterate through the records
    for record in records:
        # If the record is "+", add the current visitor to the set
        if record == "+":
            visitors.add(len(visitors))
        # If the record is "-", remove the current visitor from the set
        elif record == "-":
            visitors.remove(len(visitors) - 1)

    # Return the minimum number of distinct visitors
    return len(visitors)

