
def is_possible(W, S, C, K):
    # Initialize variables
    wolf_count = W
    sheep_count = S
    cabbage_count = C
    boat_capacity = K
    
    # Check if the input is valid
    if W < 0 or S < 0 or C < 0 or K < 0:
        return "NO"
    
    # Check if the total number of items is less than or equal to the boat capacity
    if W + S + C > boat_capacity:
        return "NO"
    
    # Check if there is a possibility to transport all the items without losing any
    if wolf_count == 0 and sheep_count == 0 and cabbage_count == 0:
        return "YES"
    if wolf_count == 0 and sheep_count == 0 and cabbage_count > 0:
        return "YES"
    if wolf_count == 0 and sheep_count > 0 and cabbage_count == 0:
        return "YES"
    if wolf_count > 0 and sheep_count == 0 and cabbage_count == 0:
        return "YES"
    if wolf_count > 0 and sheep_count > 0 and cabbage_count == 0:
        return "YES"
    if wolf_count == 0 and sheep_count > 0 and cabbage_count > 0:
        return "YES"
    if wolf_count > 0 and sheep_count == 0 and cabbage_count > 0:
        return "YES"
    if wolf_count > 0 and sheep_count > 0 and cabbage_count > 0:
        return "YES"
    
    # If none of the above conditions are met, return "NO"
    return "NO"

if __name__ == '__main__':
    W, S, C, K = map(int, input().split())
    print(is_possible(W, S, C, K))

