
def get_largest_number_of_battles(num_solar_systems, total_ships, enemy_ships):
    # Sort the enemy ships in descending order
    enemy_ships.sort(reverse=True)
    
    # Initialize the number of battles won to 0
    battles_won = 0
    
    # Loop through each solar system
    for i in range(num_solar_systems):
        # If Atli has more ships than the enemy, he wins the battle
        if total_ships > enemy_ships[i]:
            battles_won += 1
            total_ships -= enemy_ships[i]
    
    return battles_won

def main():
    num_solar_systems, total_ships = map(int, input().split())
    enemy_ships = list(map(int, input().split()))
    print(get_largest_number_of_battles(num_solar_systems, total_ships, enemy_ships))

if __name__ == '__main__':
    main()

