
def get_equal_ratings(n, ratings):
    # Sort the ratings in descending order
    ratings.sort(reverse=True)
    # Initialize the final ratings and the number of matches to play
    final_ratings = [0] * n
    matches = 0
    # Loop through the ratings and form parties of size 2 to 5
    for i in range(n):
        for j in range(i+1, n):
            matches += 1
            if ratings[i] != ratings[j]:
                final_ratings[i] += 1
                final_ratings[j] += 1
                if final_ratings[i] > final_ratings[j]:
                    final_ratings[j] = final_ratings[i]
                else:
                    final_ratings[i] = final_ratings[j]
    return final_ratings, matches

def get_matches(n, final_ratings):
    matches = []
    for i in range(n):
        match = [0] * n
        for j in range(n):
            if i != j and final_ratings[i] != final_ratings[j]:
                match[j] = 1
        matches.append("".join(map(str, match)))
    return matches

def main():
    n = int(input())
    ratings = list(map(int, input().split()))
    final_ratings, matches = get_equal_ratings(n, ratings)
    print(*final_ratings)
    print(matches)
    for match in get_matches(n, final_ratings):
        print(match)

if __name__ == '__main__':
    main()

