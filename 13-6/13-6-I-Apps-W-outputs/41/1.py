
def is_rated(n, ratings):
    # Check if at least one rating has changed
    if len(set(ratings)) == 1:
        return "unrated"
    
    # Check if the round was rated and a participant with lower rating took a better place than a participant with higher rating
    for i in range(n-1):
        if ratings[i] > ratings[i+1] and ratings[i] != ratings[i+1]:
            return "rated"
    
    # Check if the participants took places in non-increasing order of their rating
    for i in range(n-1):
        if ratings[i] < ratings[i+1]:
            return "maybe"
    
    # If none of the above conditions are met, the round is unrated
    return "unrated"

def main():
    n = int(input())
    ratings = list(map(int, input().split()))
    print(is_rated(n, ratings))

if __name__ == '__main__':
    main()

