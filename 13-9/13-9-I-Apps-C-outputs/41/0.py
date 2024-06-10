
import itertools

def explosion(n, m, d):
    # Calculate the probability of a single minion being killed
    prob_single = d / (n + m)
    
    # Calculate the probability of all minions being killed
    prob_all = 1
    for i in range(m):
        prob_all -= prob_single
    
    return prob_all

def main():
    n, m, d = map(int, input().split())
    my_health = list(map(int, input().split()))
    opponent_health = list(map(int, input().split()))
    
    print(explosion(n, m, d))

if __name__ == '__main__':
    main()

