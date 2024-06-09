
import itertools

def f1(n, m, d):
    # Calculate the probability of removing all opponent's minions
    # using the Explosion spell
    prob = 0
    for perm in itertools.permutations(range(m)):
        # For each permutation of the opponent's minions, calculate
        # the probability of removing all minions
        prob_perm = 1
        for i in range(m):
            # Calculate the probability of removing the ith minion
            prob_i = (d - sum(perm[:i])) / (m - i)
            prob_perm *= prob_i
        prob += prob_perm
    return prob

def f2(n, m, d):
    # Calculate the probability of removing all opponent's minions
    # using the Explosion spell, taking into account the fact that
    # the damage is distributed randomly across all minions
    prob = 0
    for perm in itertools.permutations(range(m)):
        # For each permutation of the opponent's minions, calculate
        # the probability of removing all minions
        prob_perm = 1
        for i in range(m):
            # Calculate the probability of removing the ith minion
            prob_i = (d - sum(perm[:i])) / (m - i)
            prob_perm *= prob_i
        prob += prob_perm
    return prob

if __name__ == '__main__':
    n, m, d = map(int, input().split())
    print(f2(n, m, d))

