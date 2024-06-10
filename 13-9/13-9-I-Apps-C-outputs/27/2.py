
def get_minimum_chairs(n, left_req, right_req):
    # Initialize variables
    total_chairs = 0
    current_chairs = 0
    circles = []
    
    # Iterate through the guests
    for i in range(n):
        # Calculate the minimum number of chairs required for the current guest
        min_chairs = left_req[i] + right_req[i] + 1
        
        # Check if the current guest can be seated in the current circle
        if current_chairs + min_chairs <= total_chairs:
            # Add the guest to the current circle
            current_chairs += min_chairs
        else:
            # Start a new circle
            circles.append(current_chairs)
            current_chairs = min_chairs
            total_chairs += min_chairs
    
    # Add the last circle
    circles.append(current_chairs)
    
    return total_chairs

def main():
    n = int(input())
    left_req = []
    right_req = []
    
    for i in range(n):
        l, r = map(int, input().split())
        left_req.append(l)
        right_req.append(r)
    
    print(get_minimum_chairs(n, left_req, right_req))

if __name__ == '__main__':
    main()

