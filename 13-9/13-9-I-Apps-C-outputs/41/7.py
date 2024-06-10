
import random

def explosion_damage(opponent_health, d):
    
    return random.sample(opponent_health, k=d)

def opponent_minions_removed(opponent_health, d):
    
    total_damage = sum(explosion_damage(opponent_health, d))
    return total_damage / sum(opponent_health)

def main():
    n, m, d = map(int, input().split())
    opponent_health = list(map(int, input().split()))
    print(round(opponent_minions_removed(opponent_health, d), 6))

if __name__ == '__main__':
    main()

