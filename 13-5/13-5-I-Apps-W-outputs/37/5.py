
def get_network_coverage(a, b):
    # Calculate the total number of households that need coverage
    total_households = sum(a)
    
    # Initialize the number of households that have been covered
    covered_households = 0
    
    # Iterate through the cities and stations
    for i in range(len(a)):
        # Calculate the number of households that can be covered by the current station
        covered_households += min(b[i], a[i])
        
        # If the number of covered households is greater than the total number of households, return False
        if covered_households > total_households:
            return False
    
    # If all households have been covered, return True
    return True

def main():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        
        print("YES") if get_network_coverage(a, b) else print("NO")

if __name__ == '__main__':
    main()

