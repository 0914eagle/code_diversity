
def get_max_candies(n, k, M, D):
    # Initialize variables
    max_candies = 0
    x = 1
    
    # Iterate through possible values of x
    while x <= M:
        # Calculate the number of candies each person will receive
        candies_per_person = x
        total_candies = 0
        for i in range(k):
            total_candies += candies_per_person
        
        # Check if the number of candies is divisible by k and if no person receives candies more than D times
        if total_candies % k == 0 and total_candies // k <= D:
            max_candies = max(max_candies, total_candies)
        
        # Increment x by 1
        x += 1
    
    # Return the maximum number of candies Arkady can receive
    return max_candies

def main():
    n, k, M, D = map(int, input().split())
    print(get_max_candies(n, k, M, D))

if __name__ == '__main__':
    main()

