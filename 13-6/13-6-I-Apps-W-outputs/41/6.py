
def is_rated(n, ratings):
    # Initialize variables
    changed_rating = False
    decreasing_rating = True

    # Check if at least one rating has changed
    for i in range(n - 1):
        if ratings[i] != ratings[i + 1]:
            changed_rating = True
            break

    # Check if the participants took places in non-increasing order of their rating
    for i in range(n - 1):
        if ratings[i] < ratings[i + 1]:
            decreasing_rating = False
            break

    # Return the result
    if changed_rating:
        return "rated"
    elif decreasing_rating:
        return "unrated"
    else:
        return "maybe"

def main():
    n = int(input())
    ratings = []
    for i in range(n):
        ratings.append(int(input()))
    print(is_rated(n, ratings))

if __name__ == '__main__':
    main()

