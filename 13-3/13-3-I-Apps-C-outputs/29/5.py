
import math

def archimedes_spiral(b, t_x, t_y):
    # Calculate the angle of the spiral at the target point
    theta = math.atan2(t_y, t_x)

    # Calculate the radius of the spiral at the target point
    r = b * theta

    # Calculate the x and y coordinates of the point on the spiral where the avatar should leave
    x = r * math.cos(theta)
    y = r * math.sin(theta)

    return x, y

def main():
    b, t_x, t_y = map(float, input().split())
    x, y = archimedes_spiral(b, t_x, t_y)
    print(x, y)

if __name__ == '__main__':
    main()

