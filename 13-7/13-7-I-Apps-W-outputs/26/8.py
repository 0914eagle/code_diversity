
def get_min_magic_points(health, spells):
    # Initialize a priority queue to store the spells
    pq = [(spell[1], spell[0]) for spell in spells]
    heapq.heapify(pq)

    # Initialize the total magic points to 0
    total_magic_points = 0

    # Loop until the monster's health becomes 0 or below
    while health > 0:
        # Pop the top spell from the priority queue
        spell_cost, spell_damage = heapq.heappop(pq)

        # Add the spell cost to the total magic points
        total_magic_points += spell_cost

        # Decrease the monster's health by the spell damage
        health -= spell_damage

    # Return the total magic points
    return total_magic_points

def main():
    # Read the input from stdin
    health, num_spells = map(int, input().split())
    spells = []
    for _ in range(num_spells):
        spell_damage, spell_cost = map(int, input().split())
        spells.append((spell_damage, spell_cost))

    # Call the get_min_magic_points function
    min_magic_points = get_min_magic_points(health, spells)

    # Print the result
    print(min_magic_points)

if __name__ == '__main__':
    main()

