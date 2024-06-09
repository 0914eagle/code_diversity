
def solve(n, ratings):
    # Sort the ratings in descending order
    ratings.sort(reverse=True)
    # Initialize the final rating and the number of matches
    R = 0
    t = 0
    # Loop through the ratings and form parties of size 2 to 5
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    # Calculate the final rating of the party
                    R_party = max(ratings[i], ratings[j], ratings[k], ratings[l])
                    # Check if the party's rating is higher than the current final rating
                    if R_party > R:
                        # Update the final rating and the number of matches
                        R = R_party
                        t += 1
                        # Print the party's composition
                        print("1111"[i] + "1111"[j] + "1111"[k] + "1111"[l])
    # Return the final rating and the number of matches
    return R, t

