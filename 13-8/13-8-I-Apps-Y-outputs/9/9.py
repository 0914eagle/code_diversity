
def get_max_candies(n, k):
    # Initialize variables
    min_candies = 0
    max_candies = 0
    total_candies = 0
    
    # Loop through each possible number of candies for each kid
    for i in range(1, n + 1):
        # Calculate the total number of candies given to kids with i candies
        total_candies += i * (k // i)
        
        # If the total number of candies is greater than the current maximum, update the maximum
        if total_candies > max_candies:
            max_candies = total_candies
            min_candies = i
    
    # Calculate the maximum number of candies that Santa can give to kids while being satisfied
    max_satisfied_candies = max_candies - (min_candies - 1) * (k // min_candies)
    
    return max_satisfied_candies

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        print(get_max_candies(n, k))

if __name__ == '__main__':
    main()

