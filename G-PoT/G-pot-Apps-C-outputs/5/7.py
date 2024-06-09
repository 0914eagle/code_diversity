
from fractions import Fraction

def calculate_probability(Tg, Ty, Tr, n, observations, tq, cq):
    cycle_length = Tg + Ty + Tr
    possible_T = []
    
    for i in range(n):
        t, color = observations[i]
        if color == 'green':
            possible_T.append((t - Tg) % cycle_length)
        elif color == 'yellow':
            possible_T.append((t - Ty) % cycle_length)
        elif color == 'red':
            possible_T.append((t - Tr) % cycle_length)
    
    tq_mod = tq % cycle_length
    count = 0
    total = 0
    
    for T in possible_T:
        if T == tq_mod:
            count += 1
        total += 1
    
    probability = Fraction(count, total)
    return float(probability)

# Input
Tg, Ty, Tr = map(int, input().split())
n = int(input())
observations = []
for _ in range(n):
    t, color = input().split()
    observations.append((int(t), color))
tq, cq = input().split()
tq = int(tq)

# Output
print(calculate_probability(Tg, Ty, Tr, n, observations, tq, cq))
