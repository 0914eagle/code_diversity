
def f1(m, essay, n, synonym_dict):
    # Initialize a dictionary to store the synonyms of each word
    synonyms = {}
    for word in essay.split():
        synonyms[word] = []

    # Add the synonyms to the dictionary
    for i in range(n):
        x, y = synonym_dict[i].split()
        synonyms[x].append(y)
        synonyms[y].append(x)

    # Replace the words in the essay with their synonyms
    for word in essay.split():
        if word in synonyms:
            essay = essay.replace(word, synonyms[word][0])

    # Count the number of letters 'r' in the essay
    count_r = essay.lower().count('r')

    # Return the count of letters 'r' and the length of the essay
    return count_r, len(essay)

def f2(m, essay, n, synonym_dict):
    # Initialize a dictionary to store the synonyms of each word
    synonyms = {}
    for word in essay.split():
        synonyms[word] = []

    # Add the synonyms to the dictionary
    for i in range(n):
        x, y = synonym_dict[i].split()
        synonyms[x].append(y)
        synonyms[y].append(x)

    # Replace the words in the essay with their synonyms
    for word in essay.split():
        if word in synonyms:
            essay = essay.replace(word, synonyms[word][0])

    # Count the number of letters 'r' in the essay
    count_r = essay.lower().count('r')

    # Return the count of letters 'r' and the length of the essay
    return count_r, len(essay)

if __name__ == '__main__':
    m = int(input())
    essay = input()
    n = int(input())
    synonym_dict = [input() for _ in range(n)]
    count_r, length = f1(m, essay, n, synonym_dict)
    print(count_r, length)

