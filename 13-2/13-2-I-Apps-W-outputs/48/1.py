
def solve(logs, cuts):
    # Sort the logs in non-decreasing order
    logs.sort()
    # Initialize the longest log length to 0
    longest_log = 0
    # Loop through each log and calculate the longest length after at most K cuts
    for log in logs:
        # Calculate the number of cuts needed for this log
        num_cuts = (log - 1) // cuts
        # Calculate the length of the longest log after the cuts
        longest_log = max(longest_log, log - num_cuts * cuts)
    # Return the rounded up longest log length
    return int(longest_log)

