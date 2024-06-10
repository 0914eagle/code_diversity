
def solve(H, N, A, B):
    # Initialize the minimum total Magic Points to consume
    min_magic_points = 0
    # Initialize the current health of the monster
    current_health = H
    # Loop through each spell
    for i in range(N):
        # Calculate the total cost of the spell
        total_cost = A[i] + B[i]
        # Check if the total cost is less than or equal to the current health of the monster
        if total_cost <= current_health:
            # Subtract the total cost from the current health of the monster
            current_health -= total_cost
            # Add the total cost to the minimum total Magic Points to consume
            min_magic_points += total_cost
    # Return the minimum total Magic Points to consume
    return min_magic_points

def main():
    # Read the input
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # Solve the problem
    result = solve(H, N, A, B)
    # Output the result
    print(result)

if __name__ == '__main__':
    main()

