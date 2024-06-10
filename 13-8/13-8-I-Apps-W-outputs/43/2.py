
def is_rebel_able(r, b, k):
    # Initialize a list to store the colors of the planks
    colors = []
    
    # Iterate through the planks and determine their colors
    for i in range(10**100):
        if i % r == 0 and i % b == 0:
            colors.append("RB")
        elif i % r == 0:
            colors.append("R")
        elif i % b == 0:
            colors.append("B")
        else:
            colors.append("-")
    
    # Initialize a variable to store the number of consecutive planks with the same color
    consecutive_count = 0
    
    # Iterate through the colors and check for consecutive planks with the same color
    for i in range(len(colors)):
        if colors[i] == colors[i-1]:
            consecutive_count += 1
        else:
            consecutive_count = 1
        
        # If the number of consecutive planks with the same color is greater than or equal to k, return False
        if consecutive_count >= k:
            return False
    
    # If no consecutive planks with the same color are found, return True
    return True

def main():
    # Read the number of test cases
    num_cases = int(input())
    
    # Iterate through the test cases
    for _ in range(num_cases):
        # Read the input
        r, b, k = map(int, input().split())
        
        # Determine if the execution is unavoidable
        if is_rebel_able(r, b, k):
            print("OBEY")
        else:
            print("REBEL")

if __name__ == '__main__':
    main()

