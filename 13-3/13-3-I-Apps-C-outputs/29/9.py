
import math

def archimedes_spiral(b, t_x, t_y):
    # Calculate the angle at which the avatar should leave the spiral
    theta = math.atan2(t_y, t_x)

    # Calculate the distance from the origin to the target
    r = math.sqrt(t_x**2 + t_y**2)

    # Calculate the distance from the origin to the point on the spiral where the avatar should leave it
    d = r * math.cos(theta) / b

    # Calculate the x and y coordinates of the point on the spiral where the avatar should leave it
    x = d * math.sin(theta)
    y = d * math.cos(theta)

    return x, y

def main():
    b = float(input())
    t_x = float(input())
    t_y = float(input())

    x, y = archimedes_spiral(b, t_x, t_y)
    print(x, y)

if __name__ == '__main__':
    main()

