
def solve(logs, cuts):
    # Sort the logs by length in non-decreasing order
    logs.sort()
    # Initialize the longest log length to 0
    longest_log_length = 0
    # Loop through each log and calculate the longest length after at most K cuts
    for log in logs:
        # Calculate the number of cuts needed for this log
        num_cuts = (log - 1) // cuts
        # Calculate the length of the longest log after the cuts
        longest_log_length = max(longest_log_length, log - num_cuts * cuts)
    # Return the rounded up length of the longest log
    return int(longest_log_length)

