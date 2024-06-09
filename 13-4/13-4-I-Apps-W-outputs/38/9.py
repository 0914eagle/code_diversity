
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

    # Count the number of letters 'r' in the replaced essay
    count = 0
    for word in replaced_essay:
        count += word.lower().count("r")

    return count

def f2(essay, synonyms):
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

    # Calculate the length of the replaced essay
    length = 0
    for word in replaced_essay:
        length += len(word)

    return length

if __name__ == '__main__':
    essay = input().split()
    synonyms = []
    for _ in range(int(input())):
        synonyms.append(input().split())

    count = f1(essay, synonyms)
    length = f2(essay, synonyms)

    print(count, length)

