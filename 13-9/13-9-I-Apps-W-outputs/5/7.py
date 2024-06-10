
import sys

def get_input():
    n, k = map(int, input().split())
    lamps = []
    for i in range(n):
        l, r = map(int, input().split())
        lamps.append((l, r))
    return n, k, lamps

def solve(n, k, lamps):
    # Initialize the answer to 0
    ans = 0
    
    # Iterate over all possible combinations of lamps
    for combination in combinations(lamps, k):
        # Check if the combination meets the criteria
        if all(lamp[1] >= sum(map(lambda x: x[0], combination)) for lamp in combination):
            # Increment the answer
            ans += 1
    
    # Return the answer modulo 998244353
    return ans % 998244353

def main():
    # Get the input
    n, k, lamps = get_input()
    
    # Solve the problem
    ans = solve(n, k, lamps)
    
    # Print the answer
    print(ans)

if __name__ == '__main__':
    main()

