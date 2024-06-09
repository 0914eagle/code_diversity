
from fractions import Fraction

def calculate_probability(Tg, Ty, Tr, n, observations, tq, cq):
    colors = {'green': 0, 'yellow': 1, 'red': 2}
    cycle_length = Tg + Ty + Tr
    possible_T = set()

    for t, color in observations:
        for i in range(3):
            T = t - (colors[color] - i) * cycle_length
            if T >= 0:
                possible_T.add(T % cycle_length)

    count = 0
    for T in possible_T:
        if (T <= tq and tq < T + Tg) or (T + Tg <= tq and tq < T + Tg + Ty) or (T + Tg + Ty <= tq and tq < T + Tg + Ty + Tr):
            count += 1

    probability = Fraction(count, len(possible_T))
    return float(probability) if cq == 'green' else 1 - float(probability)

# Input parsing
Tg, Ty, Tr = map(int, input().split())
n = int(input())
observations = [input().split() for _ in range(n)]
tq, cq = input().split()

# Calculate and print the probability
result = calculate_probability(Tg, Ty, Tr, n, observations, int(tq), cq)
print(result)
