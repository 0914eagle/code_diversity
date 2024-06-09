
def get_fuel_required(n, m, a, b):
    # Initialize the fuel required
    fuel_required = 0
    
    # Loop through each planet
    for i in range(n):
        # Calculate the fuel required for take-off from the current planet
        fuel_required += m * a[i] / b[i]
        
        # Calculate the fuel required for landing on the current planet
        fuel_required += m * b[i] / a[i]
    
    return fuel_required

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    print(get_fuel_required(n, m, a, b))

if __name__ == '__main__':
    main()

