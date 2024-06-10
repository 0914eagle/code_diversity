
def solve(H, N, A, B):
    # Initialize the minimum total Magic Points to consume
    min_magic_points = 0
    # Initialize the current health of the monster
    current_health = H
    # Loop through each spell
    for i in range(N):
        # Calculate the cost of the spell in Magic Points
        cost = B[i]
        # Calculate the decrease in health from the spell
        decrease = A[i]
        # Check if casting the spell will result in a win
        if current_health - decrease <= 0:
            # If the spell will result in a win, add its cost to the minimum total Magic Points
            min_magic_points += cost
            # Break out of the loop
            break
        # Otherwise, cast the spell and update the current health
        current_health -= decrease
    # Return the minimum total Magic Points to consume
    return min_magic_points

def main():
    # Read the input H, N, A, and B from stdin
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # Solve the problem
    min_magic_points = solve(H, N, A, B)
    # Print the minimum total Magic Points to consume
    print(min_magic_points)

if __name__ == '__main__':
    main()

