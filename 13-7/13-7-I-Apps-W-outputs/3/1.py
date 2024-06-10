
def read_input():
    N = int(input())
    S = list(map(int, input().split()))
    return N, S

def set_healths(N, S):
    # Initialize the health of the first slime
    healths = [S[0]]
    # Loop through the remaining elements of S
    for i in range(1, len(S)):
        # Find the smallest health that is greater than or equal to the current sum of the healths
        health = next((x for x in range(1, 10**9+1) if x >= sum(healths)), 10**9+1)
        # If no such health exists, return False
        if health == 10**9+1:
            return False
        # Add the health to the list of healths
        healths.append(health)
    # If the length of the list of healths is not equal to 2^N, return False
    if len(healths) != 2**N:
        return False
    # Return True if the multiset of the healths is equal to S, and False otherwise
    return sorted(healths) == sorted(S)

def main():
    N, S = read_input()
    print("Yes") if set_healths(N, S) else print("No")

if __name__ == '__main__':
    main()

