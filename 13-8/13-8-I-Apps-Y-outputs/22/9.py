
def solve(A):
    # Initialize a set to store the numbers on the sheet
    numbers = set()
    
    # Iterate through the input array
    for a in A:
        # If the number is already on the sheet, remove it
        if a in numbers:
            numbers.remove(a)
        # Otherwise, add it to the sheet
        else:
            numbers.add(a)
    
    # Return the number of numbers on the sheet
    return len(numbers)

def main():
    # Read the input data
    N = int(input())
    A = [int(x) for x in input().split()]
    
    # Solve the problem
    result = solve(A)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

