
def get_final_rating(n, ratings):
    # Sort the ratings in descending order
    ratings.sort(reverse=True)
    # Calculate the sum of the ratings
    sum_ratings = sum(ratings)
    # Calculate the average rating
    avg_rating = sum_ratings / n
    # Calculate the difference between the average rating and each rating
    diff_ratings = [abs(rating - avg_rating) for rating in ratings]
    # Return the final rating as the sum of the differences
    return sum(diff_ratings)

def get_optimal_strategy(n, ratings):
    # Initialize the final rating and the optimal strategy
    final_rating = 0
    optimal_strategy = []
    
    # Loop through each rating and calculate the final rating and the optimal strategy
    for i in range(n):
        # Calculate the final rating for the current rating and the previous final rating
        final_rating += abs(ratings[i] - final_rating)
        # Add the current rating to the optimal strategy
        optimal_strategy.append(ratings[i])
    
    # Return the final rating and the optimal strategy
    return final_rating, optimal_strategy

def main():
    # Read the input n and the ratings from stdin
    n = int(input())
    ratings = list(map(int, input().split()))
    
    # Get the final rating and the optimal strategy
    final_rating, optimal_strategy = get_optimal_strategy(n, ratings)
    
    # Print the final rating and the optimal strategy
    print(final_rating)
    print(len(optimal_strategy))
    for rating in optimal_strategy:
        print("1" * rating + "0" * (n - rating))

if __name__ == '__main__':
    main()

