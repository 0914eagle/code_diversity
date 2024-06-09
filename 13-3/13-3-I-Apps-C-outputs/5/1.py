
def get_min_fuel(n, m, a, b):
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
        # Subtract the fuel that has been burned from the rocket's mass
        m -= takeoff_fuel * a[i] + landing_fuel * b[i]
    return fuel

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(get_min_fuel(n, m, a, b))

if __name__ == '__main__':
    main()

