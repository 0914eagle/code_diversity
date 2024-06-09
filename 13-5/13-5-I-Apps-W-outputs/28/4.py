
def f1(n):
    # Initialize a list to store the number of ways to fill each row
    ways = [0] * (n + 1)
    ways[0] = 1
    
    # Loop through each row
    for i in range(1, n + 1):
        # Loop through each column in the current row
        for j in range(i + 1):
            # If the current column is not the last column, add the number of ways to fill the current column to the total number of ways
            if j < i:
                ways[i] += ways[j]
            # If the current column is the last column, add the number of ways to fill the current column to the total number of ways
            else:
                ways[i] += 1
    
    # Return the total number of ways to fill the tiles
    return ways[n]

def f2(...):
    # Your code here
    pass

if __name__ == '__main__':
    n = int(input())
    print(f1(n))

