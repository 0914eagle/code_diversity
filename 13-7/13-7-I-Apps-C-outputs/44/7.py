
def get_final_ratings(n, ratings):
    # Sort the ratings in descending order
    ratings.sort(reverse=True)
    
    # Initialize the final ratings and the number of matches to play
    final_ratings = [0] * n
    num_matches = 0
    
    # Iterate through the ratings and form parties of size 2 to 5
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    # Form a party of size 4 and play a match
                    party = [ratings[i], ratings[j], ratings[k], ratings[l]]
                    party.sort(reverse=True)
                    num_matches += 1
                    
                    # Update the final ratings
                    for m in range(4):
                        final_ratings[m] = max(final_ratings[m], party[m])
    
    return final_ratings, num_matches

def get_match_schedule(n, final_ratings, num_matches):
    # Initialize the match schedule
    match_schedule = []
    
    # Iterate through the final ratings and form parties of size 2 to 5
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    # Form a party of size 4 and add it to the match schedule
                    party = [i, j, k, l]
                    party.sort()
                    match_schedule.append(party)
    
    # Shuffle the match schedule
    import random
    random.shuffle(match_schedule)
    
    # Return the first num_matches parties from the match schedule
    return match_schedule[:num_matches]

if __name__ == '__main__':
    n = int(input())
    ratings = list(map(int, input().split()))
    final_ratings, num_matches = get_final_ratings(n, ratings)
    match_schedule = get_match_schedule(n, final_ratings, num_matches)
    print(*final_ratings)
    print(num_matches)
    for party in match_schedule:
        print(''.join('1' if i in party else '0' for i in range(n)))

