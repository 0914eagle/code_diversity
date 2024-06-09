
def f1(W, S, C, K):
    # Initialize variables
    wolf_count = W
    sheep_count = S
    cabbage_count = C
    boat_capacity = K
    loss_items = False

    # Check if the number of items is less than or equal to the boat capacity
    if wolf_count + sheep_count + cabbage_count <= boat_capacity:
        return "YES"

    # Check if the number of wolves is less than or equal to the boat capacity
    if wolf_count <= boat_capacity:
        wolf_count = 0
        sheep_count += W
        cabbage_count += W

    # Check if the number of sheep is less than or equal to the boat capacity
    if sheep_count <= boat_capacity:
        sheep_count = 0
        cabbage_count += S

    # Check if the number of cabbages is less than or equal to the boat capacity
    if cabbage_count <= boat_capacity:
        cabbage_count = 0

    # Check if any items have been lost
    if wolf_count + sheep_count + cabbage_count > 0:
        loss_items = True

    # Return the result
    if loss_items:
        return "NO"
    else:
        return "YES"

