
def power(x, y):
    return x ** y

def sum_of_costs(n, k):
    # Calculate the sum of costs for all non-empty subsets
    total_cost = 0
    for i in range(1, n + 1):
        total_cost += power(i, k)
    return total_cost

def main():
    n, k = map(int, input().split())
    print(sum_of_costs(n, k))

if __name__ == '__main__':
    main()

