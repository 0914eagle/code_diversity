
def f1(n, k, a):
    # Calculate the sum of the initial cows
    sum_a = sum(a)
    
    # Initialize the winner as Kevin
    winner = "Kevin"
    
    # Loop through each pile of cows
    for i in range(n):
        # If the pile has an even number of cows, calculate the number of piles that can be created
        if a[i] % 2 == 0:
            num_piles = a[i] // 2
            
            # If the number of piles is greater than or equal to k, the winner is Nicky
            if num_piles >= k:
                winner = "Nicky"
                break
    
    # If the winner is still Kevin, check if Nicky can win by removing the last cow
    if winner == "Kevin":
        # If the sum of the cows is odd, Nicky can win by removing the last cow
        if sum_a % 2 == 1:
            winner = "Nicky"
    
    return winner

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(f1(n, k, a))

