
def solve(n, initial_order, target_order):
    # Convert the input permutations to lists
    initial_order = list(map(int, initial_order.split()))
    target_order = list(map(int, target_order.split()))
    
    # Check if the target order is a rotation of the initial order
    if target_order == initial_order[len(initial_order) - len(target_order):] + target_order[:len(initial_order) - len(target_order)]:
        return "Possible"
    else:
        return "Impossible"

