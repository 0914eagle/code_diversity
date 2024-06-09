
import math

def get_average_path_length(towns):
    num_towns = len(towns)
    total_length = 0
    for i in range(num_towns):
        for j in range(i+1, num_towns):
            x1, y1 = towns[i]
            x2, y2 = towns[j]
            total_length += math.sqrt((x1-x2)**2 + (y1-y2)**2)
    return total_length / math.factorial(num_towns)

towns = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    towns.append((x, y))

print(get_average_path_length(towns))

