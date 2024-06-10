
def get_minimum_magic_points(health, spells):
    # Initialize a list to store the minimum magic points required to cast each spell
    min_magic_points = [spell[1] for spell in spells]

    # Loop through the spells in descending order of their costs
    for i in range(len(spells) - 1):
        # Get the current spell and its cost
        spell = spells[i]
        cost = spell[1]

        # Loop through the remaining spells
        for j in range(i + 1, len(spells)):
            # Get the next spell and its cost
            next_spell = spells[j]
            next_cost = next_spell[1]

            # If the current spell's cost is greater than the next spell's cost,
            # update the minimum magic points required to cast the current spell
            if cost > next_cost:
                min_magic_points[i] = min(min_magic_points[i], min_magic_points[j] + cost - next_cost)

    # Return the minimum magic points required to cast the first spell
    return min_magic_points[0]

def main():
    health, num_spells = map(int, input().split())
    spells = []
    for _ in range(num_spells):
        spell = list(map(int, input().split()))
        spells.append(spell)
    print(get_minimum_magic_points(health, spells))

if __name__ == '__main__':
    main()

