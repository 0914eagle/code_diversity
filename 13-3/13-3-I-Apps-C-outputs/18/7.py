
def f1(W, S, C, K):
    # Initialize variables
    wolf_count = W
    sheep_count = S
    cabbage_count = C
    boat_capacity = K
    loss_occured = False

    # While there are still items to transport
    while wolf_count > 0 or sheep_count > 0 or cabbage_count > 0:
        # If the boat is full, unload all items
        if wolf_count + sheep_count + cabbage_count > boat_capacity:
            wolf_count -= 1
            sheep_count -= 1
            cabbage_count -= 1
        # If there are still items to transport, load them into the boat
        else:
            wolf_count -= 1
            sheep_count -= 1
            cabbage_count -= 1

        # If a loss has occurred, break the loop
        if wolf_count < 0 or sheep_count < 0 or cabbage_count < 0:
            loss_occured = True
            break

    # If a loss has occurred, return NO, otherwise return YES
    if loss_occured:
        return "NO"
    else:
        return "YES"

def f2(...):
    # Implement function f2 here
    pass

if __name__ == '__main__':
    W, S, C, K = map(int, input().split())
    print(f1(W, S, C, K))

