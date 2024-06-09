
import itertools

def get_combinations(switches, bulbs):
    num_combinations = 0
    for combination in itertools.product([0, 1], repeat=len(switches)):
        is_lighted = True
        for i, state in enumerate(combination):
            if state == 1:
                for j in range(bulbs[i][0]):
                    if combination[bulbs[i][j+1]-1] == 0:
                        is_lighted = False
                        break
        if is_lighted:
            num_combinations += 1
    return num_combinations

if __name__ == '__main__':
    switches, bulbs, p = [], [], []
    for line in iter(input, ''):
        if line.startswith('N'):
            N = int(line.split()[1])
        elif line.startswith('M'):
            M = int(line.split()[1])
        elif line.startswith('k'):
            switches.append(list(map(int, line.split()[1:])))
        elif line.startswith('s'):
            bulbs.append(list(map(int, line.split()[1:])))
        elif line.startswith('p'):
            p.append(int(line.split()[1]))
    print(get_combinations(switches, bulbs))

