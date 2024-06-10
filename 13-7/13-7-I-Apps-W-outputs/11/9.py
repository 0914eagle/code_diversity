
import math

def calculate_distance(t):
    # Calculate the distance between Agneta and Beata at time t
    distance = math.sqrt((agneta_x(t) - beata_x(t))**2 + (agneta_y(t) - beata_y(t))**2)
    return distance

def agneta_x(t):
    # Calculate Agneta's x-coordinate at time t
    x = 1 + t * math.sin(agneta_angular_speed * t)
    return x

def agneta_y(t):
    # Calculate Agneta's y-coordinate at time t
    y = t * math.cos(agneta_angular_speed * t)
    return y

def beata_x(t):
    # Calculate Beata's x-coordinate at time t
    x = 2 + t * math.sin(beata_angular_speed * t)
    return x

def beata_y(t):
    # Calculate Beata's y-coordinate at time t
    y = t * math.cos(beata_angular_speed * t)
    return y

def main():
    # Read input
    W = float(input())

    # Calculate the minimal distance between Agneta and Beata
    minimal_distance = calculate_distance(W)

    # Print output
    print(minimal_distance)

if __name__ == '__main__':
    main()

