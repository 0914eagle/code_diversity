
def power_sum(N, k):
    # Calculate the sum of costs for all non-empty subsets
    total_cost = 0
    for i in range(1, N+1):
        total_cost += (i**k) % (10**9 + 7)
    return total_cost

def main():
    N, k = map(int, input().split())
    print(power_sum(N, k))

if __name__ == '__main__':
    main()

