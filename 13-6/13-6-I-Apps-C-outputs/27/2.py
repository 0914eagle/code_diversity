
def get_order(n, m, k, a):
    # Initialize the permutation as the identity permutation
    order = list(range(1, n+1))
    
    # Loop through each critic and their initial score
    for i in range(n):
        # Calculate the average score given by the previous critics
        avg_score = (k - a[i]) / (n - i - 1)
        
        # If the average score is less than or equal to the initial score,
        # the current critic will give a score of m
        if avg_score <= a[i]:
            # Find the index of the current critic in the permutation
            index = order.index(i+1)
            
            # Swap the current critic with the last critic in the permutation
            order[index] = order[-1]
            order[n-1] = i+1
    
    return order

def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    order = get_order(n, m, k, a)
    print(*order)

if __name__ == '__main__':
    main()

