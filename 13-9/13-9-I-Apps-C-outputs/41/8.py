
import math

def get_probability(n, m, d, my_health, enemy_health):
    # Calculate the total number of minions that will be affected by the explosion
    total_affected = n + m
    
    # Calculate the probability that a single minion will be affected by the explosion
    prob_affected = 1 / total_affected
    
    # Calculate the probability that a single minion will survive the explosion
    prob_survive = (my_health + enemy_health) / (my_health + enemy_health + d)
    
    # Calculate the probability that all minions will survive the explosion
    prob_all_survive = prob_survive ** total_affected
    
    # Calculate the probability that all minions will be removed by the explosion
    prob_all_removed = 1 - prob_all_survive
    
    return prob_all_removed

def main():
    n, m, d = map(int, input().split())
    my_health = list(map(int, input().split()))
    enemy_health = list(map(int, input().split()))
    print(get_probability(n, m, d, my_health, enemy_health))

if __name__ == '__main__':
    main()

