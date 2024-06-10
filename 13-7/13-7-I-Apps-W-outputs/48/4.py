
def solve(n, m, r, s, b):
    # Initialize the maximum profit
    max_profit = 0
    
    # Loop through all possible ways to buy and sell shares
    for i in range(n):
        for j in range(m):
            # Calculate the profit from buying and selling shares
            profit = r + s[i] - b[j]
            
            # Update the maximum profit
            max_profit = max(max_profit, profit)
    
    # Return the maximum profit
    return max_profit

def main():
    # Read the input
    n, m, r = map(int, input().split())
    s = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    # Solve the problem
    max_profit = solve(n, m, r, s, b)
    
    # Print the output
    print(max_profit)

if __name__ == '__main__':
    main()

