
def can_paint_fence(r, b, k):
    # Initialize a list to store the painted planks
    painted_planks = []
    
    # Loop through all the planks
    for i in range(10**100):
        # Check if the current plank is divisible by r and b
        if i % r == 0 and i % b == 0:
            # If both conditions are true, choose a color at random
            color = "red" if random.randint(0, 1) == 0 else "blue"
        elif i % r == 0:
            # If the current plank is divisible by r, paint it red
            color = "red"
        elif i % b == 0:
            # If the current plank is divisible by b, paint it blue
            color = "blue"
        else:
            # If the current plank is not divisible by r or b, don't paint it
            continue
        
        # Add the painted plank to the list
        painted_planks.append(color)
    
    # Check if there are k consecutive planks with the same color in the list
    for i in range(len(painted_planks) - k + 1):
        # If there are k consecutive planks with the same color, return False
        if len(set(painted_planks[i:i+k])) == 1:
            return False
    
    # If there are no k consecutive planks with the same color, return True
    return True

def main():
    # Read the number of test cases
    num_cases = int(input())
    
    # Loop through each test case
    for _ in range(num_cases):
        # Read the coefficients r, b, and k
        r, b, k = map(int, input().split())
        
        # Check if the fence can be painted
        if can_paint_fence(r, b, k):
            print("OBEY")
        else:
            print("REBEL")

if __name__ == '__main__':
    main()

