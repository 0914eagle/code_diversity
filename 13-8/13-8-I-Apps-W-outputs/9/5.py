
def max_cuts(numbers, budget):
    # Sort the numbers in ascending order
    numbers.sort()
    # Initialize variables to keep track of the current cost and the maximum number of cuts
    cost, max_cuts = 0, 0
    # Iterate through the numbers and check if the current cost is less than or equal to the budget
    for i in range(len(numbers)-1):
        cost += abs(numbers[i+1] - numbers[i])
        if cost <= budget:
            max_cuts += 1
    # Return the maximum number of cuts that can be made with the given budget
    return max_cuts

