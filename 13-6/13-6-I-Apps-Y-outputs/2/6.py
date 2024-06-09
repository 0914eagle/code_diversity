
def refill_fridge(n, m, s, d, current_slots):
    # Initialize the probability of all students getting a cold soda to 0
    prob_cold = 0
    # Initialize the number of cold sodas in the fridge to 0
    num_cold = 0
    # Initialize the number of new sodas to add to the fridge
    num_new = n
    # Initialize the refill scheme as an empty list
    refill_scheme = []

    # Loop through each slot in the fridge
    for i in range(s):
        # If the current slot has some sodas in it
        if current_slots[i] > 0:
            # Add the number of cold sodas in the current slot to the total number of cold sodas in the fridge
            num_cold += current_slots[i]
            # If the number of cold sodas in the current slot is greater than or equal to the number of new sodas to add
            if current_slots[i] >= num_new:
                # Add the number of new sodas to add to the refill scheme for the current slot
                refill_scheme.append(num_new)
                # Subtract the number of new sodas from the number of sodas in the current slot
                current_slots[i] -= num_new
                # Set the number of new sodas to add to 0
                num_new = 0
                # Break out of the loop
                break
            # If the number of cold sodas in the current slot is less than the number of new sodas to add
            else:
                # Add the number of cold sodas in the current slot to the refill scheme for the current slot
                refill_scheme.append(current_slots[i])
                # Subtract the number of cold sodas in the current slot from the number of new sodas to add
                num_new -= current_slots[i]
                # Set the number of cold sodas in the current slot to 0
                current_slots[i] = 0

    # If there are still new sodas to add
    if num_new > 0:
        # Loop through each slot in the fridge
        for i in range(s):
            # If the current slot has some space left
            if current_slots[i] < d:
                # Add the number of new sodas to add to the refill scheme for the current slot
                refill_scheme.append(num_new)
                # Subtract the number of new sodas from the number of sodas in the current slot
                current_slots[i] += num_new
                # Break out of the loop
                break

    # Calculate the probability of all students getting a cold soda
    prob_cold = num_cold / (num_cold + m)

    # If the probability of all students getting a cold soda is greater than or equal to 1
    if prob_cold >= 1:
        # Return the refill scheme
        return refill_scheme
    # If the probability of all students getting a cold soda is less than 1
    else:
        # Return "impossible"
        return "impossible"

