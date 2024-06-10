
def get_min_magic_points(health, spells):
    # Initialize a list to store the minimum magic points needed to win for each spell
    min_magic_points = [0] * len(spells)
    # Initialize a list to store the minimum health needed to win for each spell
    min_health = [0] * len(spells)
    
    # Loop through each spell and calculate the minimum magic points needed to win
    for i in range(len(spells)):
        # Calculate the minimum health needed to win after casting this spell
        min_health[i] = health - spells[i][0]
        # Calculate the minimum magic points needed to win after casting this spell
        min_magic_points[i] = spells[i][1]
        # Loop through each previous spell and compare the minimum health and magic points needed to win
        for j in range(i):
            # If casting this spell reduces the minimum health needed to win, update the minimum health
            if min_health[i] < min_health[j]:
                min_health[j] = min_health[i]
            # If casting this spell reduces the minimum magic points needed to win, update the minimum magic points
            if min_magic_points[i] < min_magic_points[j]:
                min_magic_points[j] = min_magic_points[i]
    
    # Return the minimum total magic points needed to win
    return sum(min_magic_points)

def main():
    health, num_spells = map(int, input().split())
    spells = []
    for _ in range(num_spells):
        spell = list(map(int, input().split()))
        spells.append(spell)
    print(get_min_magic_points(health, spells))

if __name__ == '__main__':
    main()

