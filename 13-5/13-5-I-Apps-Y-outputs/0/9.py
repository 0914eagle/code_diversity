
def get_min_attacks(healths, k):
    # Initialize variables
    attacks = 0
    special_moves = k
    total_health = sum(healths)
    
    # Loop through the healths and check if any monster is defeated
    while total_health > 0:
        # Check if any monster is defeated and update the total health
        for i in range(len(healths)):
            if healths[i] <= 0:
                total_health -= healths[i]
                healths[i] = 0
        
        # If all monsters are defeated, return the number of attacks
        if total_health == 0:
            return attacks
        
        # If special move is available, use it on the weakest monster
        if special_moves > 0:
            special_moves -= 1
            healths[healths.index(min(healths))] = 0
            total_health -= min(healths)
        
        # Otherwise, attack the strongest monster
        else:
            attacks += 1
            healths[healths.index(max(healths))] -= 1
    
    # If all monsters are not defeated, return -1
    return -1

def main():
    n, k = map(int, input().split())
    healths = list(map(int, input().split()))
    print(get_min_attacks(healths, k))

if __name__ == '__main__':
    main()

