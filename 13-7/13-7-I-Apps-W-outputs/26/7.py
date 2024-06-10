
def read_input():
    H, N = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        A_i, B_i = map(int, input().split())
        A.append(A_i)
        B.append(B_i)
    return H, N, A, B

def solve(H, N, A, B):
    # Initialize the minimum total Magic Points to be consumed
    min_MP = 0
    # Loop through each spell and check if casting it will decrease the monster's health
    for i in range(N):
        # Calculate the new health after casting the spell
        new_health = H - A[i]
        # If the new health is 0 or below, add the cost of the spell to the minimum total Magic Points
        if new_health <= 0:
            min_MP += B[i]
            # Break out of the loop since we have already found a way to win
            break
    return min_MP

def main():
    H, N, A, B = read_input()
    print(solve(H, N, A, B))

if __name__ == '__main__':
    main()

