
def solve(a, x):
    # Calculate the greatest common divisor (gcd) of the elements in a
    gcd = a[0]
    for i in range(1, len(a)):
        gcd = gcd_recursive(gcd, a[i])
    
    # Initialize the count of pairs (l, r) with 0
    count = 0
    
    # Iterate over each query x_i
    for i in range(len(x)):
        # Initialize the left and right indices for the current query
        l, r = 0, 0
        
        # Iterate over each element in a and check if the gcd is equal to x_i
        while r < len(a):
            if gcd_recursive(gcd, a[r]) == x[i]:
                count += 1
            r += 1
        
        # Print the count of pairs for the current query
        print(count)
    
    return count

def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)

a = [2, 6, 3]
x = [5, 1, 2, 3, 4, 6]
solve(a, x)

