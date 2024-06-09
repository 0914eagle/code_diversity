
def solve(n, m, likes, weights):
    # Calculate the sum of all weights
    total_weight = sum(weights)
    
    # Create a dictionary to store the likes and weights of each picture
    picture_likes = {}
    for i in range(n):
        picture_likes[i] = {
            "like": likes[i],
            "weight": weights[i]
        }
    
    # Loop through each visit
    for visit in range(m):
        # Calculate the probability of each picture being displayed
        probabilities = [picture["weight"] / total_weight for picture in picture_likes.values()]
        
        # Choose a picture randomly based on the probabilities
        choice = np.random.choice(n, p=probabilities)
        
        # Update the weight of the chosen picture
        picture_likes[choice]["weight"] += 1 if picture_likes[choice]["like"] else -1
    
    # Calculate the expected weight of each picture
    expected_weights = [picture["weight"] / (visit + 1) for visit, picture in picture_likes.items()]
    
    # Return the expected weights modulo 998244353
    return [expected_weight % 998244353 for expected_weight in expected_weights]

