
def is_rated(n, ratings):
    # Initialize variables
    prev_rating = ratings[0][0]
    changed = False
    
    # Iterate through the ratings
    for i in range(1, n):
        curr_rating = ratings[i][0]
        if curr_rating != prev_rating:
            changed = True
        if curr_rating < ratings[i][1]:
            return "rated"
        prev_rating = curr_rating
    
    # Check if the round was rated
    if changed:
        return "rated"
    
    # Check if the round was unrated
    if all(ratings[i][0] == ratings[i][1] for i in range(n)):
        return "unrated"
    
    # It's impossible to determine whether the round is rated or not
    return "maybe"

def main():
    n = int(input())
    ratings = []
    for i in range(n):
        ratings.append(list(map(int, input().split())))
    print(is_rated(n, ratings))

if __name__ == '__main__':
    main()

