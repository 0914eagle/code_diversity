
def get_max_damage(n, a, b, health, damage):
    # Initialize the maximum total damage
    max_damage = 0
    
    # Loop through each creature
    for i in range(n):
        # Use the first spell on the creature
        health[i] *= 2
        damage[i] += health[i]
        max_damage += damage[i]
        
        # Use the second spell on the creature
        if a > 0:
            a -= 1
            health[i] = damage[i]
            damage[i] = 0
            max_damage += health[i]
    
    # Return the maximum total damage
    return max_damage

def main():
    n, a, b = map(int, input().split())
    health = list(map(int, input().split()))
    damage = list(map(int, input().split()))
    print(get_max_damage(n, a, b, health, damage))

if __name__ == '__main__':
    main()

