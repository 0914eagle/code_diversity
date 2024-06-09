
def get_moon_status(n, records):
    # Convert the records to a list of integers
    records = [int(x) for x in records]

    # Check if the length of the records is greater than or equal to n
    if len(records) < n:
        return -1

    # Get the last n records
    last_n_records = records[-n:]

    # Check if the last n records form a cycle
    if len(set(last_n_records)) == len(last_n_records):
        return -1

    # Get the next record
    next_record = last_n_records[0]

    # Check if the next record is less than the current record
    if next_record < last_n_records[-1]:
        return "DOWN"
    elif next_record > last_n_records[-1]:
        return "UP"
    else:
        return -1

