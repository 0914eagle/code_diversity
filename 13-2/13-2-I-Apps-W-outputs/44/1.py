
def is_moon_down(n, records):
    # Convert the records to a list of integers
    records = [int(x) for x in records]

    # Check if the length of the records is valid
    if len(records) != n:
        return -1

    # Check if the records are in the correct order
    if not all(records[i] < records[i+1] for i in range(len(records)-1)):
        return -1

    # Check if the records form a cycle
    if records[0] != records[-1]:
        return -1

    # Check if the next day's record is less than the current day's record
    if records[0] < records[-1]:
        return "DOWN"
    else:
        return "UP"

