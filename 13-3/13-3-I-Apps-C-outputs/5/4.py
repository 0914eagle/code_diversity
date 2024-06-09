
def get_min_fuel(n, m, a, b):
    # Initialize the fuel amount to 0
    fuel = 0
    # Loop through each planet
    for i in range(n):
        # Calculate the fuel needed for takeoff from the current planet
        fuel_takeoff = m // a[i]
        # Calculate the fuel needed for landing on the current planet
        fuel_landing = m // b[i]
        # Add the fuel needed for takeoff and landing to the total fuel amount
        fuel += fuel_takeoff + fuel_landing
        # Subtract the fuel consumed during takeoff and landing from the rocket's mass
        m -= fuel_takeoff * a[i] + fuel_landing * b[i]
    return fuel

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(get_min_fuel(n, m, a, b))

if __name__ == '__main__':
    main()

