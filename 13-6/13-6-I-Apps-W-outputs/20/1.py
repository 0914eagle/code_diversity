
def get_seals(doors):
    seals = []
    for door in doors:
        n = door[0]
        energies = door[1:]
        seal_combinations = [(1,) * n]
        for i in range(2, n + 1):
            seal_combinations += [(i,) * j for j in range(1, n + 1 - i)]
        for seal_combination in seal_combinations:
            if sum(seal_combination[i] * energies[i] for i in range(n)) == 0:
                seals.append(seal_combination)
                break
    return seals

