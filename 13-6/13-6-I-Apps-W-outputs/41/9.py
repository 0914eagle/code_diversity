
def is_rated(n, ratings):
    # Check if at least one rating has changed
    if len(set(ratings)) == 1:
        return "unrated"
    
    # Check if the round was rated and a participant with lower rating took a better place in the standings than a participant with higher rating
    for i in range(n-1):
        if ratings[i] > ratings[i+1] and ratings[i] - ratings[i+1] > 100:
            return "rated"
    
    # If none of the above conditions are met, it's impossible to determine whether the round is rated or not
    return "maybe"

def main():
    n = int(input())
    ratings = []
    for i in range(n):
        ratings.append(int(input()))
    print(is_rated(n, ratings))

if __name__ == '__main__':
    main()

