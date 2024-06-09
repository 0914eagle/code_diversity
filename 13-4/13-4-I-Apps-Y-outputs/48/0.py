
import itertools

def get_combinations(switches, bulbs):
    num_combinations = 0
    for combination in itertools.product([0, 1], repeat=len(switches)):
        is_lighted = True
        for i in range(len(bulbs)):
            num_switches_on = 0
            for j in range(len(bulbs[i])):
                if combination[bulbs[i][j]-1] == 1:
                    num_switches_on += 1
            if num_switches_on % 2 != bulbs[i][-1]:
                is_lighted = False
                break
        if is_lighted:
            num_combinations += 1
    return num_combinations

switches, bulbs = [], []
N, M = map(int, input().split())
for i in range(M):
    num_switches, p = map(int, input().split())
    switches_list = [int(x) for x in input().split()]
    bulbs.append([num_switches, p] + switches_list)

print(get_combinations(switches, bulbs))

