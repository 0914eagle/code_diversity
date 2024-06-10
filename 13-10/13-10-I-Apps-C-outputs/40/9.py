
import sys

def get_paintings_needed(a, b, c):
    
    # Initialize variables
    paintings_needed = 0
    colored_paintings = 0
    black_and_white_paintings = 0
    
    # Iterate through the clients
    for i in range(len(a)):
        # If the client wants colored paintings
        if a[i] > 0:
            # Add the number of colored paintings needed for this client
            paintings_needed += a[i]
            colored_paintings += 1
        
        # If the client wants black and white paintings
        if b[i] > 0:
            # Add the number of black and white paintings needed for this client
            paintings_needed += b[i]
            black_and_white_paintings += 1
    
    # If the number of colored paintings is less than the minimum requirement
    if colored_paintings < c:
        # Add the difference to the number of paintings needed
        paintings_needed += c - colored_paintings
    
    return paintings_needed

def update_paintings_needed(a, b, c, d, e):
    
    # If the client wants colored paintings
    if d > 0:
        # Add the difference to the number of colored paintings needed
        a[c-1] += d - e
    
    # If the client wants black and white paintings
    if e > 0:
        # Add the difference to the number of black and white paintings needed
        b[c-1] += e - d
    
    return a, b

def main():
    # Read the input
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    q = int(input())
    
    # Initialize the number of paintings needed
    paintings_needed = get_paintings_needed(a, b, c)
    
    # Iterate through the requirement changes
    for i in range(q):
        # Read the next requirement change
        p, d, e = map(int, input().split())
        
        # Update the number of paintings needed
        a, b = update_paintings_needed(a, b, p, d, e)
        paintings_needed = get_paintings_needed(a, b, c)
    
    # Print the number of paintings needed modulo 10007
    print(paintings_needed % 10007)

if __name__ == '__main__':
    main()

