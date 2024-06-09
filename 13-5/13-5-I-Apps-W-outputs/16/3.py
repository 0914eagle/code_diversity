
def solve(C, N, M, cows, days):
    # Initialize a list to store the number of farms to inspect on each day
    farms_to_inspect = [0] * (M + 1)
    
    # Loop through each day
    for d in range(1, M + 1):
        # Loop through each farm
        for i in range(N):
            # Check if the farm has at least one cow
            if cows[i] > 0:
                # Calculate the number of cows on the farm on this day
                num_cows = cows[i] * 2 ** (d - 1)
                # Check if the farm has more than C cows
                if num_cows > C:
                    # Calculate the number of cows to move to a new farm
                    num_cows_to_move = num_cows // 2
                    # Add the number of farms to inspect on this day
                    farms_to_inspect[d] += 1
        # Add the number of farms to inspect on this day
        farms_to_inspect[d] += N
    
    return farms_to_inspect

