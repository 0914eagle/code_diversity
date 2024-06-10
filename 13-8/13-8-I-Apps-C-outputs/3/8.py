
def cost(n, k):
    # Calculate the cost of having n people for the task
    return n ** k

def non_empty_subsets(n, k):
    # Calculate the sum of costs for all non-empty subsets of people
    return sum(cost(i, k) for i in range(1, n + 1))

def main():
    n, k = map(int, input().split())
    print(non_empty_subsets(n, k) % (10**9 + 7))

if __name__ == '__main__':
    main()

