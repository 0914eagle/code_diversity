
def read_input():
    H, N = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        A_i, B_i = map(int, input().split())
        A.append(A_i)
        B.append(B_i)
    return H, N, A, B

def solve(H, N, A, B):
    # Initialize the minimum total Magic Points to 0
    min_MP = 0
    # Initialize the current health of the monster to H
    current_health = H
    # Loop through each spell
    for i in range(N):
        # Calculate the amount of Magic Points required to cast the spell
        MP = B[i]
        # Calculate the amount of health that the spell will decrease the monster's health by
        decrease_health = A[i]
        # Check if casting the spell will decrease the monster's health to 0 or below
        if current_health - decrease_health <= 0:
            # If it will, break the loop
            break
        # Otherwise, update the minimum total Magic Points required
        min_MP += MP
        # Update the current health of the monster
        current_health -= decrease_health
    # Return the minimum total Magic Points required
    return min_MP

def main():
    H, N, A, B = read_input()
    print(solve(H, N, A, B))

if __name__ == '__main__':
    main()

