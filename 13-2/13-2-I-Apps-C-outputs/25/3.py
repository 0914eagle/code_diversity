
import itertools

def f1(n, m, d):
    # Calculate the probability of removing all opponent's minions
    # using the Explosion spell
    prob = 0
    for healths in itertools.product(range(1, 7), repeat=m):
        # Calculate the number of minions that will be removed
        # by the Explosion spell
        num_removed = 0
        for i in range(d):
            if sum(healths) - i > 0:
                num_removed += 1
        # If all opponent's minions are removed, add the probability
        if num_removed == m:
            prob += 1 / (6 ** m)
    return prob

def f2(n, m, d):
    # Calculate the probability of removing all opponent's minions
    # using the Explosion spell, taking into account the fact that
    # all your own minions may die in the process
    prob = 0
    for healths in itertools.product(range(1, 7), repeat=m):
        # Calculate the number of minions that will be removed
        # by the Explosion spell
        num_removed = 0
        for i in range(d):
            if sum(healths) - i > 0:
                num_removed += 1
        # If all opponent's minions are removed, add the probability
        if num_removed == m:
            prob += 1 / (6 ** m)
    return prob

if __name__ == '__main__':
    n, m, d = map(int, input().split())
    print(f1(n, m, d))
    print(f2(n, m, d))

