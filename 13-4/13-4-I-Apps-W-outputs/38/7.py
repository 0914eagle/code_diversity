
def f1(essay, synonyms):
    # Initialize a dictionary to store the synonyms
    synonym_dict = {}
    for synonym in synonyms:
        synonym_dict[synonym[0]] = synonym[1]

    # Replace the words in the essay with their synonyms
    new_essay = []
    for word in essay:
        if word in synonym_dict:
            new_essay.append(synonym_dict[word])
        else:
            new_essay.append(word)

    return " ".join(new_essay)

def f2(essay):
    # Count the number of letters "r" in the essay
    count = 0
    for word in essay:
        count += word.lower().count("r")

    return count

if __name__ == '__main__':
    essay = input().split()
    synonyms = [input().split() for _ in range(int(input()))]
    new_essay = f1(essay, synonyms)
    count = f2(new_essay)
    print(count)

