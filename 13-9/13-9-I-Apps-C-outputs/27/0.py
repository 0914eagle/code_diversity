
def solve(n, m, a, w):
    # Calculate the total weight of all pictures
    total_weight = sum(w)

    # Initialize the expected weights
    expected_weights = [0] * n

    # Loop through each visit
    for i in range(m):
        # Choose a picture randomly based on its weight
        chosen_picture = random.choices(population=range(n), weights=w, k=1)[0]

        # If the chosen picture is liked, increase its weight by 1
        if a[chosen_picture] == 1:
            w[chosen_picture] += 1

        # If the chosen picture is not liked, decrease its weight by 1
        else:
            w[chosen_picture] -= 1

        # Calculate the new expected weight for each picture
        for j in range(n):
            expected_weights[j] += w[j] / total_weight

    # Return the expected weights modulo 998244353
    return [int(998244353 * x) % 998244353 for x in expected_weights]

