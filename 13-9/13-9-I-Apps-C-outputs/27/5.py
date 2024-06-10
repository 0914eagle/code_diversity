
def get_total_chairs(n, left_reqs, right_reqs):
    # Calculate the total number of chairs required
    total_chairs = 0
    for i in range(n):
        total_chairs += left_reqs[i] + right_reqs[i] + 1
    
    return total_chairs

def get_min_chairs(n, left_reqs, right_reqs):
    # Initialize the minimum number of chairs as the total number of chairs required
    min_chairs = get_total_chairs(n, left_reqs, right_reqs)
    
    # Iterate through all possible combinations of circles
    for i in range(1, n+1):
        # Calculate the total number of chairs required for the current combination of circles
        total_chairs = 0
        for j in range(n):
            total_chairs += left_reqs[j] + right_reqs[j] + 1
        
        # If the current combination of circles requires fewer chairs than the minimum, update the minimum
        if total_chairs < min_chairs:
            min_chairs = total_chairs
    
    return min_chairs

def main():
    n = int(input())
    left_reqs = []
    right_reqs = []
    for i in range(n):
        left_req, right_req = map(int, input().split())
        left_reqs.append(left_req)
        right_reqs.append(right_req)
    print(get_min_chairs(n, left_reqs, right_reqs))

if __name__ == '__main__':
    main()

