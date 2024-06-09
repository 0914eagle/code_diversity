
import math

def archimedes_spiral(b, t_x, t_y):
    # Calculate the angle of the spiral at the target point
    theta = math.atan2(t_y, t_x)

    # Calculate the distance from the origin to the target point
    r = math.hypot(t_x, t_y)

    # Calculate the angle of the spiral at the point where the avatar should leave the spiral
    phi = math.acos(r / (b * theta))

    # Calculate the x and y coordinates of the point where the avatar should leave the spiral
    x = b * phi * math.cos(theta)
    y = b * phi * math.sin(theta)

    return x, y

def main():
    b, t_x, t_y = map(float, input().split())
    x, y = archimedes_spiral(b, t_x, t_y)
    print(f"{x:.9f} {y:.9f}")

if __name__ == "__main__":
    main()

