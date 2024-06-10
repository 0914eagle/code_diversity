
def solve(n, a, p):
    # Calculate the sum of the guests' sizes
    sum_a = sum(a)
    
    # Initialize a list to store the number of visitors for each possible order
    num_visitors = [0] * n
    
    # Iterate over all possible orders
    for i in range(n):
        # Calculate the sum of the guests' sizes for the current order
        curr_sum = sum(a[j] for j in range(i, n))
        
        # Check if the current order fits at the table
        if curr_sum <= p:
            # Add the number of guests in the current order to the list
            num_visitors[i] = i + 1
        else:
            # Add the number of guests that fit in the current order to the list
            num_visitors[i] = (p - sum_a + a[i]) // a[i]
    
    # Calculate the average number of visitors
    avg_visitors = sum(num_visitors) / n
    
    return avg_visitors

def main():
    n, a, p = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, a, p))

if __name__ == '__main__':
    main()

