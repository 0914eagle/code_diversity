
def get_minimum_cashes(visitors):
    # Sort the visitors by their arrival time
    visitors.sort(key=lambda x: x[0])
    
    # Initialize the number of cashes as 1
    cashes = 1
    
    # Iterate through the visitors
    for i in range(len(visitors)):
        # If the current visitor's arrival time is greater than the previous visitor's arrival time, then we need to add another cash
        if i > 0 and visitors[i][0] > visitors[i-1][0]:
            cashes += 1
    
    return cashes

def main():
    visitors = []
    
    # Read the number of visitors
    n = int(input())
    
    # Read the arrival times of the visitors
    for i in range(n):
        h, m = map(int, input().split())
        visitors.append((h, m))
    
    # Get the minimum number of cashes needed to serve all visitors
    cashes = get_minimum_cashes(visitors)
    
    # Print the result
    print(cashes)

if __name__ == '__main__':
    main()

