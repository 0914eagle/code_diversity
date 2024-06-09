
def get_lawn_width(n, s, g):
    # Initialize the total width of lawns to remove
    total_width = 0
    
    # Initialize the new widths of the road
    s_prime = [0] * n
    
    # Loop through each part of the street
    for i in range(n):
        # Calculate the maximum width of lawn that can be removed without violating the condition
        max_width = min(s[i], g[i])
        
        # Add the width of the lawn to the total width of lawns to remove
        total_width += max_width
        
        # Update the new width of the road
        s_prime[i] = s[i] + max_width
    
    return total_width, s_prime

def solve(n, s, g):
    # Initialize the total width of lawns to remove
    total_width = 0
    
    # Loop through each part of the street
    for i in range(n):
        # Calculate the maximum width of lawn that can be removed without violating the condition
        max_width = min(s[i], g[i])
        
        # Add the width of the lawn to the total width of lawns to remove
        total_width += max_width
    
    return total_width

def main():
    n = int(input())
    s = list(map(int, input().split()))
    g = list(map(int, input().split()))
    
    total_width, s_prime = get_lawn_width(n, s, g)
    
    if total_width == -1:
        print(-1)
    else:
        print(total_width)
        print(*s_prime)

if __name__ == '__main__':
    main()

