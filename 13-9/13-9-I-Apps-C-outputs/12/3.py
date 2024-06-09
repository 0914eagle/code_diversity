
import math

def traffic_lights(n, x, r, g):
    # Calculate the probability that the car will make it through all the lights
    probability = 1
    for i in range(n):
        if x[i] <= 0:
            probability *= (1 - r[i] / (r[i] + g[i]))
        else:
            probability *= r[i] / (r[i] + g[i])
    
    # Calculate the probability that the car will hit the first red light
    first_red_light = 0
    for i in range(n):
        if x[i] <= 0:
            first_red_light += r[i] / (r[i] + g[i])
    
    return probability, first_red_light

n = int(input())
x = []
r = []
g = []
for i in range(n):
    xi, ri, gi = map(int, input().split())
    x.append(xi)
    r.append(ri)
    g.append(gi)

probability, first_red_light = traffic_lights(n, x, r, g)
print(f"{probability:.6f}")
print(f"{first_red_light:.6f}")

