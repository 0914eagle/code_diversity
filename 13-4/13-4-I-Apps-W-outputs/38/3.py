
def f1(essay, synonyms):
    # Initialize a dictionary to store the synonyms
    synonym_dict = {}
    for synonym in synonyms:
        synonym_dict[synonym[0]] = synonym[1]

    # Replace the words in the essay with their synonyms
    replaced_essay = []
    for word in essay:
        if word in synonym_dict:
            replaced_essay.append(synonym_dict[word])
        else:
            replaced_essay.append(word)

    # Return the replaced essay
    return replaced_essay

def f2(essay):
    # Initialize a variable to store the minimum number of Rs
    min_rs = float('inf')

    # Initialize a variable to store the minimum length
    min_length = float('inf')

    # Iterate through all possible combinations of synonyms
    for i in range(len(essay)):
        for j in range(i+1, len(essay)):
            # Check if the combination of synonyms is valid
            if essay[i] != essay[j] and essay[i] in synonyms and essay[j] in synonyms[essay[i]]:
                # Replace the words with their synonyms
                replaced_essay = f1(essay, [(essay[i], essay[j])])

                # Calculate the number of Rs in the replaced essay
                num_rs = sum(1 for word in replaced_essay if 'r' in word.lower())

                # Calculate the length of the replaced essay
                length = sum(len(word) for word in replaced_essay)

                # Check if the current combination is the optimal one
                if num_rs < min_rs or (num_rs == min_rs and length < min_length):
                    min_rs = num_rs
                    min_length = length

    # Return the minimum number of Rs and the minimum length
    return min_rs, min_length

if __name__ == '__main__':
    essay = input().split()
    synonyms = [tuple(input().split()) for _ in range(int(input()))]
    print(*f2(essay))

