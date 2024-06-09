
def can_reach_n1(n, m, d, c):
    # Initialize the array a as all zeros
    a = [0] * (n + 2)
    
    # Initialize the number of jumps as 0
    jumps = 0
    
    # Loop through each platform
    for i in range(m):
        # Get the length of the current platform
        length = c[i]
        
        # Loop through each cell in the platform
        for j in range(length):
            # Get the current cell number
            cell = i + j + 1
            
            # If the cell is not the last cell in the platform, set the next cell to 1
            if j < length - 1:
                a[cell] = 1
            
            # If the cell is the last cell in the platform, set the next cell to 2
            else:
                a[cell] = 2
    
    # Loop through each cell in the array a
    for i in range(n + 2):
        # If the current cell is 1, check if the next d cells are also 1
        if a[i] == 1:
            for j in range(i + 1, i + d + 1):
                # If any of the next d cells are not 1, break the loop
                if a[j] != 1:
                    break
            
            # If all the next d cells are 1, set the current cell to 0
            else:
                a[i] = 0
        
        # If the current cell is 2, check if the previous d cells are also 2
        if a[i] == 2:
            for j in range(i - 1, i - d - 1, -1):
                # If any of the previous d cells are not 2, break the loop
                if a[j] != 2:
                    break
            
            # If all the previous d cells are 2, set the current cell to 0
            else:
                a[i] = 0
    
    # Check if the first cell is 0
    if a[0] == 0:
        # If the first cell is 0, return YES and the array a
        return "YES\n" + " ".join(map(str, a))
    
    # If the first cell is not 0, return NO
    else:
        return "NO"

def main():
    # Read the input n, m, and d
    n, m, d = map(int, input().split())
    
    # Read the input c
    c = list(map(int, input().split()))
    
    # Call the can_reach_n1 function and print the result
    print(can_reach_n1(n, m, d, c))

if __name__ == '__main__':
    main()

