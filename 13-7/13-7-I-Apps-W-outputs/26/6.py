
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
    # Initialize the minimum total Magic Points to consume
    min_MP = 0
    # Initialize the current health of the monster
    current_health = H
    # Loop through each spell
    for i in range(N):
        # Calculate the health of the monster after casting the spell
        new_health = current_health - A[i]
        # If the monster's health is 0 or below after casting the spell, we have found the minimum total Magic Points to consume
        if new_health <= 0:
            return min_MP + B[i]
        # Otherwise, update the minimum total Magic Points to consume and the current health of the monster
        min_MP += B[i]
        current_health = new_health
    # If we reach this point, we have not found a solution, so return -1
    return -1

def main():
    H, N, A, B = read_input()
    print(solve(H, N, A, B))

if __name__ == '__main__':
    main()

