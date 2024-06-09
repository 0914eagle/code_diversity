
def get_minimum_fuel(n, m, a, b):
    # Initialize the fuel required for each planet
    fuel_required = [0] * (n + 1)
    fuel_required[1] = m
    
    # Loop through each planet and calculate the fuel required for take-off and landing
    for i in range(1, n):
        fuel_required[i + 1] += fuel_required[i] // a[i] * b[i]
        fuel_required[i + 1] += fuel_required[i] % a[i]
    
    # Return the minimum fuel required
    return min(fuel_required)

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(get_minimum_fuel(n, m, a, b))

if __name__ == '__main__':
    main()

