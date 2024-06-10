
def get_min_extensions(a, b, h, w, n, a_list):
    # Initialize variables
    min_extensions = 0
    current_h = h
    current_w = w
    
    # Iterate through the available extensions
    for i in range(n):
        # Check if the current extension can be used to increase the width
        if a_list[i] <= current_w:
            current_w *= a_list[i]
            min_extensions += 1
        
        # Check if the current extension can be used to increase the height
        if a_list[i] <= current_h:
            current_h *= a_list[i]
            min_extensions += 1
        
        # Check if the rectangle can be placed on the current field
        if current_w >= a and current_h >= b:
            break
    
    # Return the minimum number of extensions needed to reach Arkady's goal
    return min_extensions

def main():
    a, b, h, w, n = map(int, input().split())
    a_list = list(map(int, input().split()))
    print(get_min_extensions(a, b, h, w, n, a_list))

if __name__ == '__main__':
    main()

