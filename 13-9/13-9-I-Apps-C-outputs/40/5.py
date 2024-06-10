
import math

def is_valid_walk(walk, L, N):
    # Check if the walk is valid
    if len(walk) != L:
        return False
    
    for i in range(L):
        if walk[i] < 0 or walk[i] >= N:
            return False
    
    for i in range(L - 1):
        if walk[i] == walk[i + 1]:
            return False
    
    return True

def count_valid_walks(L, N):
    # Count the number of valid walks
    count = 0
    for i in range(N):
        for j in range(N):
            if i != j:
                walk = [i, j]
                if is_valid_walk(walk, L, N):
                    count += 1
    
    return count

def calculate_chance(L, N):
    # Calculate the chance of success
    valid_walks = count_valid_walks(L, N)
    total_walks = math.factorial(N)
    chance = valid_walks / total_walks
    return chance

def main():
    N, L = map(int, input().split())
    walk = list(map(int, input().split()))
    print(calculate_chance(L, N))

if __name__ == '__main__':
    main()

