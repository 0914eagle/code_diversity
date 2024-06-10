
def count_valid_pairs(n, k):
    count = 0
    toy_costs = {}
    
    for i in range(1, n + 1):
        toy_costs[i] = True
    
    for i in range(1, n + 1):
        if k - i in toy_costs and k - i != i:
            count += 1
    
    return count

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(count_valid_pairs(n, k))
