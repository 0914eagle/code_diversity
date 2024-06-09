
def get_minimum_fuel(n, m, a, b):
    # Initialize the fuel amount to 0
    fuel = 0
    # Loop through each planet
    for i in range(n):
        # Calculate the fuel needed for takeoff from the current planet
        takeoff_fuel = m // a[i]
        # Calculate the fuel needed for landing on the current planet
        landing_fuel = m // b[i]
        # Add the fuel needed for takeoff and landing to the total fuel amount
        fuel += takeoff_fuel + landing_fuel
        # Update the mass of the rocket after takeoff and landing
        m -= takeoff_fuel * a[i] + landing_fuel * b[i]
    # Return the minimum fuel amount needed
    return fuel

def main():
    # Read the input data
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # Calculate the minimum fuel amount
    fuel = get_minimum_fuel(n, m, a, b)
    # Print the result
    print(fuel)

if __name__ == '__main__':
    main()

