
def f1(m, essay, n, synonyms):
    # Initialize a dictionary to store the synonyms
    synonym_dict = {}
    for synonym in synonyms:
        synonym_dict[synonym[0]] = synonym[1]

    # Initialize a set to store the words that can be replaced
    replaceable_words = set()
    for word in essay.split():
        if word.lower() in synonym_dict:
            replaceable_words.add(word)

    # Initialize a list to store the optimal essay
    optimal_essay = []

    # Iterate through the essay and replace the replaceable words with their synonyms
    for word in essay.split():
        if word.lower() in replaceable_words:
            optimal_essay.append(synonym_dict[word.lower()])
        else:
            optimal_essay.append(word)

    # Return the optimal essay and the number of letters 'r' in it
    return " ".join(optimal_essay), optimal_essay.count("r")

def f2(m, essay, n, synonyms):
    # Initialize a dictionary to store the synonyms
    synonym_dict = {}
    for synonym in synonyms:
        synonym_dict[synonym[0]] = synonym[1]

    # Initialize a set to store the words that can be replaced
    replaceable_words = set()
    for word in essay.split():
        if word.lower() in synonym_dict:
            replaceable_words.add(word)

    # Initialize a list to store the optimal essay
    optimal_essay = []

    # Iterate through the essay and replace the replaceable words with their synonyms
    for word in essay.split():
        if word.lower() in replaceable_words:
            optimal_essay.append(synonym_dict[word.lower()])
        else:
            optimal_essay.append(word)

    # Return the optimal essay and the length of it
    return " ".join(optimal_essay), len(" ".join(optimal_essay))

if __name__ == '__main__':
    m = int(input())
    essay = input()
    n = int(input())
    synonyms = [input().split() for _ in range(n)]
    print(f1(m, essay, n, synonyms))
    print(f2(m, essay, n, synonyms))

