
def f1(W, S, C, K):
    # Initialize variables
    wolf_count = W
    sheep_count = S
    cabbage_count = C
    boat_capacity = K
    loss_occured = False

    # Check if the number of wolves is greater than the number of sheep
    if wolf_count > sheep_count:
        loss_occured = True

    # Check if the number of sheep is greater than the number of cabbages
    if sheep_count > cabbage_count:
        loss_occured = True

    # Check if the sum of the number of wolves, sheep, and cabbages is greater than the boat capacity
    if wolf_count + sheep_count + cabbage_count > boat_capacity:
        loss_occured = True

    # Return the result
    if loss_occured:
        return "NO"
    else:
        return "YES"

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    W, S, C, K = map(int, input().split())
    print(f1(W, S, C, K))

