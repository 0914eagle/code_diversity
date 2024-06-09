
def round_to_nearest(candy_cost, smallest_bill):
    # Convert the candy cost to a string
    cost_str = str(candy_cost)
    
    # Find the index of the first non-zero digit in the string
    non_zero_index = 0
    for i in range(len(cost_str)):
        if cost_str[i] != '0':
            non_zero_index = i
            break
    
    # Round the cost to the nearest power of 10
    rounded_cost = int(cost_str[:non_zero_index + 1] + '0' * (smallest_bill - non_zero_index))
    
    return rounded_cost

