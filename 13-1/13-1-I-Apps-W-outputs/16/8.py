
def get_min_cashes(visitors):
    # Sort the visitors by their arrival time
    visitors.sort(key=lambda x: x[0])
    
    # Initialize the number of cashes as 1
    cashes = 1
    
    # Iterate through the visitors
    for i in range(len(visitors)):
        # If the current visitor's arrival time is greater than the previous visitor's arrival time, increase the number of cashes
        if visitors[i][0] > visitors[i-1][0]:
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
    
    # Call the get_min_cashes function and print the result
    print(get_min_cashes(visitors))

if __name__ == '__main__':
    main()

