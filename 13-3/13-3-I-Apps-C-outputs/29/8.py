
import math

def archimedes_spiral(b, t_x, t_y):
    # Find the angle at which the avatar should leave the spiral
    theta = math.atan2(t_y, t_x)

    # Find the distance from the origin to the target
    r = math.sqrt(t_x**2 + t_y**2)

    # Find the distance from the origin to the point on the spiral where the avatar should leave it
    d = r * math.cos(theta) / b

    # Find the coordinates of the point on the spiral where the avatar should leave it
    x = d * math.sin(theta)
    y = d * math.cos(theta)

    return x, y

def main():
    b, t_x, t_y = map(float, input().split())
    x, y = archimedes_spiral(b, t_x, t_y)
    print(f"{x:.9f} {y:.9f}")

if __name__ == "__main__":
    main()

