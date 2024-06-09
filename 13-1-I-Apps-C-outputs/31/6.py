
import math

def solve(n, omega, v0, theta, w):
    # Calculate the initial angle of the cookie in radians
    theta_rad = math.radians(theta)

    # Calculate the initial velocity of the cookie in x and y directions
    vx = v0 * math.cos(theta_rad)
    vy = v0 * math.sin(theta_rad)

    # Calculate the acceleration of the cookie in x and y directions
    ax = -omega ** 2 * math.sin(theta_rad)
    ay = omega ** 2 * math.cos(theta_rad) - 9.81

    # Calculate the time it takes for the cookie to reach the wall
    t = (w - vx) / ax

    # Calculate the position of the cookie at the time it hits the wall
    x = vx * t + 0.5 * ax * t ** 2
    y = vy * t + 0.5 * ay * t ** 2

    # Calculate the angle of the cookie at the time it hits the wall
    theta_hit = math.atan2(y, x)

    # Calculate the index of the corner that hits the wall first
    i = int(math.ceil(n * theta_hit / (2 * math.pi)))
    if i == 0:
        i = n

    # Calculate the time it takes for the corner to hit the wall
    T_i = t - (i - 1) * 2 * math.pi / omega

    return i, T_i

