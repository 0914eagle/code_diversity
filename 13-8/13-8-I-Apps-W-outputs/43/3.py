
def paint_fence(r, b, k):
    # Initialize the number of red and blue planks
    num_red = 0
    num_blue = 0
    
    # Iterate through the indices of the planks
    for i in range(100):
        # If the index is divisible by r, paint it red
        if i % r == 0:
            num_red += 1
        # If the index is divisible by b, paint it blue
        if i % b == 0:
            num_blue += 1
    
    # If the number of red planks is greater than or equal to k, return REBEL
    if num_red >= k:
        return "REBEL"
    # If the number of blue planks is greater than or equal to k, return REBEL
    if num_blue >= k:
        return "REBEL"
    # Otherwise, return OBEY
    return "OBEY"

def main():
    # Read the number of test cases
    num_cases = int(input())
    
    # Iterate through the test cases
    for _ in range(num_cases):
        # Read the coefficients r, b, and k
        r, b, k = map(int, input().split())
        
        # Call the paint_fence function and print the result
        print(paint_fence(r, b, k))

if __name__ == '__main__':
    main()

