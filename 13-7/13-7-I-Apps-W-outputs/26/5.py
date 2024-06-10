
def get_minimum_magic_points(health, spells):
    # Initialize a priority queue to store the spells
    pq = [(spell[1], spell[0]) for spell in spells]
    heapq.heapify(pq)

    # Initialize the total magic points to 0
    total_magic_points = 0

    # Loop until the monster's health is 0 or below
    while health > 0:
        # Get the next spell with the highest cost-to-damage ratio
        cost, damage = heapq.heappop(pq)

        # Add the cost to the total magic points
        total_magic_points += cost

        # Subtract the damage from the monster's health
        health -= damage

    # Return the total magic points
    return total_magic_points

def main():
    health, num_spells = map(int, input().split())
    spells = []
    for _ in range(num_spells):
        spell = list(map(int, input().split()))
        spells.append(spell)
    print(get_minimum_magic_points(health, spells))

if __name__ == '__main__':
    main()

