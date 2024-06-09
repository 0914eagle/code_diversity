
def f1(n, m, a, w):
    # Calculate the total weight of all pictures
    total_weight = sum(w)
    
    # Initialize the expected weight of each picture
    expected_weight = [0] * n
    
    # Loop through each visit
    for i in range(m):
        # Choose a picture randomly based on its weight
        picture_index = choose_picture(w)
        
        # If the chosen picture is liked by Nauuo
        if a[picture_index] == 1:
            # Increase the weight of the chosen picture by 1
            w[picture_index] += 1
        else:
            # Decrease the weight of the chosen picture by 1
            w[picture_index] -= 1
        
        # Calculate the expected weight of each picture
        for j in range(n):
            expected_weight[j] += w[j] / total_weight
    
    # Return the expected weight of each picture modulo 998244353
    return [int(round(x * 998244353)) % 998244353 for x in expected_weight]

def choose_picture(weights):
    # Calculate the cumulative weights
    cumulative_weights = [0] * len(weights)
    cumulative_weights[0] = weights[0]
    for i in range(1, len(weights)):
        cumulative_weights[i] = cumulative_weights[i-1] + weights[i]
    
    # Choose a picture randomly based on its weight
    random_weight = random.randint(1, sum(weights))
    for i in range(len(weights)):
        if random_weight <= cumulative_weights[i]:
            return i

def f2(...):
    ...

if __name__ == '__main__':
    n = ...
    m = ...
    a = ...
    w = ...
    result = f1(n, m, a, w)
    print(result)

