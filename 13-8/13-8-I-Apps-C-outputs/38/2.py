
def get_character_features(n, k, existing_characters):
    # Initialize a dictionary to store the features of Tira's character
    tira_character = {}
    
    # Iterate through the existing characters
    for character in existing_characters:
        # Initialize a set to store the features of the current character
        current_character = set()
        
        # Iterate through the features of the current character
        for j in range(k):
            # If the current character has the j'th feature, add it to the set
            if character[j] == "1":
                current_character.add(j)
        
        # Add the set of features of the current character to the dictionary
        tira_character[frozenset(current_character)] = 0
    
    # Initialize a variable to store the maximum similarity between Tira's character and any other character
    max_similarity = 0
    
    # Iterate through the features of Tira's character
    for i in range(k):
        # Initialize a set to store the features of Tira's character that are different from the i'th feature
        different_features = set(range(k))
        different_features.remove(i)
        
        # Initialize a variable to store the similarity between Tira's character and the current character
        current_similarity = 0
        
        # Iterate through the features of the current character
        for j in range(k):
            # If the current character has the j'th feature and Tira's character does not have it, increase the similarity
            if tira_character[frozenset(different_features)][j] == 1 and character[j] == "0":
                current_similarity += 1
        
        # If the similarity between Tira's character and the current character is greater than the maximum similarity, update the maximum similarity
        if current_similarity > max_similarity:
            max_similarity = current_similarity
    
    # Return the features of Tira's character with the maximum similarity
    return [int(i in tira_character[frozenset(different_features)]) for i in range(k)]

def main():
    n, k = map(int, input().split())
    existing_characters = []
    for _ in range(n):
        existing_characters.append(input())
    print("".join(str(i) for i in get_character_features(n, k, existing_characters)))

if __name__ == '__main__':
    main()

