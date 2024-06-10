
def read_input():
    H, N = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        A.append(int(input()))
        B.append(int(input()))
    return H, N, A, B

def solve(H, N, A, B):
    # Initialize the minimum total Magic Points as infinity
    min_MP = float('inf')
    # Initialize the current health of the monster as H
    current_health = H
    # Loop through each spell
    for i in range(N):
        # Calculate the cost of casting the current spell
        cost = B[i]
        # Calculate the health of the monster after casting the current spell
        new_health = current_health - A[i]
        # If the health of the monster is 0 or below, update the minimum total Magic Points
        if new_health <= 0:
            min_MP = min(min_MP, cost)
        # Otherwise, recursively call the function to cast the remaining spells
        else:
            min_MP = min(min_MP, solve(new_health, N-i, A[i:], B[i:]) + cost)
    return min_MP

def main():
    H, N, A, B = read_input()
    print(solve(H, N, A, B))

if __name__ == '__main__':
    main()

