
import sys
import itertools

def read_list(t): return [int(x) for x in sys.stdin.readline().strip().split()]
def read_matrix(n): return [read_list(t) for _ in range(n)]

def solve(n, k, a, b, t, u):
    # convert tastiness matrix to a list
    tastiness = [sum(row) for row in t]
    
    # convert cost matrix to a list
    cost = [a + b * row[0] for row in t]
    
    # find all possible combinations of flavors
    combinations = itertools.combinations(range(k), n)
    
    # calculate the total tastiness and cost for each combination
    total_tastiness = [sum(tastiness[i] for i in comb) for comb in combinations]
    total_cost = [sum(cost[i] for i in comb) for comb in combinations]
    
    # find the combination with the maximum tastiness-to-cost ratio
    best_index = total_tastiness.index(max(total_tastiness))
    best_ratio = total_tastiness[best_index] / total_cost[best_index]
    
    return best_ratio

def main():
    n, k, a, b = read_list(4)
    t = read_matrix(k)
    u = read_matrix(k)
    print(solve(n, k, a, b, t, u))

if __name__ == '__main__':
    main()

