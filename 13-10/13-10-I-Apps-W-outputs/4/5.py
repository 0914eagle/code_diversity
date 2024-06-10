
def count_swaps(n, a, p):
    # Count the number of ways to make the swap
    count = 0
    
    # Iterate over all possible pairs of nodes
    for i in range(1, n):
        for j in range(i+1, n+1):
            # Check if the nodes have different parents
            if p[i] != p[j]:
                # Check if the nodes are leaves
                if a[i] != 0 and a[j] != 0:
                    count += 1
    
    return count

def main():
    # Read the input
    n = int(input())
    a = list(map(int, input().split()))
    p = list(map(int, input().split()))
    
    # Call the count_swaps function
    count = count_swaps(n, a, p)
    
    # Print the result
    print(count)

if __name__ == '__main__':
    main()

