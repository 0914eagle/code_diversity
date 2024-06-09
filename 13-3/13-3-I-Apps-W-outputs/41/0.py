
def get_max_total_damage(n, a, b, health, damage):
    # Initialize the maximum total damage to 0
    max_total_damage = 0
    
    # Loop through each creature
    for i in range(n):
        # Calculate the total damage of the current creature
        total_damage = health[i] + damage[i]
        
        # If the total damage is greater than the maximum total damage, update the maximum total damage
        if total_damage > max_total_damage:
            max_total_damage = total_damage
    
    # Return the maximum total damage
    return max_total_damage

def main():
    # Read the input n, a, b, health, and damage
    n, a, b = map(int, input().split())
    health = list(map(int, input().split()))
    damage = list(map(int, input().split()))
    
    # Call the get_max_total_damage function and print the result
    print(get_max_total_damage(n, a, b, health, damage))

if __name__ == '__main__':
    main()

