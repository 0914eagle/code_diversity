
import math

def archimedes_spiral(b, t_x, t_y):
    # Find the angle at which the avatar should leave the spiral
    theta = math.atan2(t_y, t_x)

    # Find the point on the spiral where the avatar should leave it
    r = b * theta
    x = r * math.cos(theta)
    y = r * math.sin(theta)

    return x, y

def main():
    b, t_x, t_y = map(float, input().split())
    x, y = archimedes_spiral(b, t_x, t_y)
    print(x, y)

if __name__ == '__main__':
    main()

