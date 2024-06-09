
def is_moon_down(n, records):
    # Convert the records to a list of integers
    records = [int(x) for x in records]

    # Check if the records form a cycle
    if len(records) != 30:
        return -1

    # Check if the records are in ascending order
    if all(records[i] < records[i+1] for i in range(len(records)-1)):
        return "UP"

    # Check if the records are in descending order
    if all(records[i] > records[i+1] for i in range(len(records)-1)):
        return "DOWN"

    # If the records are not in ascending or descending order, it cannot be determined whether the moon will be up or down next day
    return -1

