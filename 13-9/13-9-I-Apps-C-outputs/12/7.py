
import math

def get_probabilities(n, x, r, g):
    # Calculate the probability that the car hits the first red light
    prob_first_red = 0
    for i in range(n):
        if i == 0:
            prob_first_red += (x[i] / r[i]) * (1 - (x[i] / r[i]))
        else:
            prob_first_red += (x[i] / r[i]) * (1 - (x[i] / r[i])) * (1 - prob_first_red)
    
    # Calculate the probability that the car makes it all the way without stopping
    prob_all_the_way = 1
    for i in range(n):
        prob_all_the_way *= 1 - (x[i] / r[i])
    
    return prob_first_red, prob_all_the_way

n = int(input())
x = []
r = []
g = []
for i in range(n):
    x_i, r_i, g_i = map(int, input().split())
    x.append(x_i)
    r.append(r_i)
    g.append(g_i)

prob_first_red, prob_all_the_way = get_probabilities(n, x, r, g)

print(prob_first_red)
print(prob_all_the_way)

