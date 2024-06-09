
def get_network_coverage(n, a, b):
    # Initialize the coverage array
    coverage = [0] * n
    
    # Iterate over each city
    for i in range(n):
        # Calculate the total number of households that need coverage
        total_households = sum(a)
        
        # Calculate the number of households that can be covered by the current station
        covered_households = min(total_households, b[i])
        
        # Update the coverage array
        coverage[i] += covered_households
        
        # Decrement the total number of households that need coverage
        total_households -= covered_households
    
    # Check if all households have been covered
    return all(coverage)

def main():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        
        if get_network_coverage(n, a, b):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()

