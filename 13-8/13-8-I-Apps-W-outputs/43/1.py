
def is_paintable(r, b, k):
    # Initialize variables
    red_count = 0
    blue_count = 0
    same_color_count = 0
    
    # Iterate through all planks
    for i in range(10**100):
        # Check if plank is divisible by r and b
        if i % r == 0 and i % b == 0:
            # Choose color randomly
            if red_count > blue_count:
                color = "red"
            else:
                color = "blue"
        elif i % r == 0:
            color = "red"
        elif i % b == 0:
            color = "blue"
        else:
            continue
        
        # Update variables
        if color == "red":
            red_count += 1
        else:
            blue_count += 1
        if red_count > 0 and blue_count > 0:
            same_color_count += 1
        
        # Check if execution is unavoidable
        if same_color_count >= k:
            return False
    
    return True

def main():
    # Read number of test cases
    num_tc = int(input())
    
    # Iterate through test cases
    for _ in range(num_tc):
        # Read input
        r, b, k = map(int, input().split())
        
        # Check if execution is unavoidable
        if is_paintable(r, b, k):
            print("OBEY")
        else:
            print("REBEL")

if __name__ == '__main__':
    main()

