
def solve(n, m, a, w):
    # Calculate the sum of the weights
    sum_w = sum(w)
    
    # Initialize the expected weights
    expected_w = [0] * n
    
    # Loop through each visit
    for i in range(m):
        # Choose a picture randomly with probability proportional to its weight
        picture = random.choices(population=range(n), weights=w, k=1)[0]
        
        # If Nauuo likes the picture, add 1 to its weight
        if a[picture]:
            w[picture] += 1
        # Otherwise, subtract 1 from its weight
        else:
            w[picture] -= 1
        
        # Calculate the expected weight of the picture
        expected_w[picture] = w[picture] * (sum_w - w[picture]) / sum_w
    
    # Return the expected weights modulo 998244353
    return [int(expected_w[i] * 998244353) % 998244353 for i in range(n)]

