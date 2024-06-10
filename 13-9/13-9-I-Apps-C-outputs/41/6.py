
import itertools

def explosion_damage(n, m, d):
    # Calculate the probability of a single minion surviving the explosion
    p_survive = 1 - (d / 6)
    
    # Calculate the probability of all minions surviving the explosion
    p_all_survive = p_survive ** m
    
    # Calculate the probability of at least one minion surviving the explosion
    p_at_least_one_survive = 1 - p_all_survive
    
    # Calculate the probability of all opponent's minions being removed
    p_all_removed = p_at_least_one_survive ** n
    
    return p_all_removed

def main():
    n, m, d = map(int, input().split())
    health_own = list(map(int, input().split()))
    health_opp = list(map(int, input().split()))
    
    print(explosion_damage(n, m, d))

if __name__ == '__main__':
    main()

