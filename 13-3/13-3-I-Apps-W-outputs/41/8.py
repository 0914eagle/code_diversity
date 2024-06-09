
def get_max_damage(n, a, b, creatures):
    # Initialize the maximum total damage as 0
    max_damage = 0
    
    # Loop through each creature
    for i in range(n):
        # Get the current creature's health and damage
        hp, dmg = creatures[i]
        
        # If the creature's health is even, double its health
        if hp % 2 == 0:
            hp *= 2
        
        # If the creature's damage is odd, assign its health to its damage
        if dmg % 2 == 1:
            dmg = hp
        
        # Add the creature's damage to the maximum total damage
        max_damage += dmg
    
    # Return the maximum total damage
    return max_damage

def main():
    # Read the input n, a, b, and the creatures' health and damage
    n, a, b = map(int, input().split())
    creatures = []
    for i in range(n):
        hp, dmg = map(int, input().split())
        creatures.append((hp, dmg))
    
    # Call the get_max_damage function and print the result
    max_damage = get_max_damage(n, a, b, creatures)
    print(max_damage)

if __name__ == '__main__':
    main()

