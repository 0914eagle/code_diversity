
def get_max_value(values, costs):
    # Sort the values in descending order
    sorted_values = sorted(values, reverse=True)
    # Sort the costs in ascending order
    sorted_costs = sorted(costs)
    # Initialize the maximum value and cost
    max_value = 0
    cost = 0
    # Iterate through the values and costs
    for value, cost in zip(sorted_values, sorted_costs):
        # If the cost is less than or equal to the value, add the value to the maximum value
        if cost <= value:
            max_value += value
        # Otherwise, add the cost to the maximum value and break the loop
        else:
            max_value += cost
            break
    # Return the maximum value
    return max_value

# Main function
if __name__ == "__main__":
    # Read the number of gems and their values and costs from stdin
    num_gems = int(input())
    values = list(map(int, input().split()))
    costs = list(map(int, input().split()))
    # Get the maximum value
    max_value = get_max_value(values, costs)
    # Print the maximum value
    print(max_value)

