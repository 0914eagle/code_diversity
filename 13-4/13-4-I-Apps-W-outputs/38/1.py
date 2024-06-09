
def f1(m, essay, n, synonyms):
    # Initialize a dictionary to store the synonyms
    synonym_dict = {}
    for synonym in synonyms:
        synonym_dict[synonym[0]] = synonym[1]

    # Initialize a set to store the words in the essay
    essay_set = set(essay.split())

    # Initialize a variable to store the minimum number of Rs
    min_rs = float('inf')

    # Initialize a variable to store the minimum length
    min_length = float('inf')

    # Iterate over all possible combinations of synonyms
    for i in range(1 << n):
        # Initialize a set to store the current combination of synonyms
        current_set = set()

        # Iterate over all bits in the current combination
        for j in range(n):
            # If the j-th bit is set, add the j-th synonym to the current set
            if i & (1 << j):
                current_set.add(synonyms[j][1])

        # If the current set is a subset of the essay set, update the minimum number of Rs and length
        if current_set.issubset(essay_set):
            current_rs = sum(1 for word in current_set if 'r' in word.lower())
            current_length = sum(len(word) for word in current_set)
            if current_rs < min_rs or (current_rs == min_rs and current_length < min_length):
                min_rs = current_rs
                min_length = current_length

    return min_rs, min_length

def f2(m, essay, n, synonyms):
    # Initialize a dictionary to store the synonyms
    synonym_dict = {}
    for synonym in synonyms:
        synonym_dict[synonym[0]] = synonym[1]

    # Initialize a set to store the words in the essay
    essay_set = set(essay.split())

    # Initialize a variable to store the minimum number of Rs
    min_rs = float('inf')

    # Initialize a variable to store the minimum length
    min_length = float('inf')

    # Iterate over all possible combinations of synonyms
    for i in range(1 << n):
        # Initialize a set to store the current combination of synonyms
        current_set = set()

        # Iterate over all bits in the current combination
        for j in range(n):
            # If the j-th bit is set, add the j-th synonym to the current set
            if i & (1 << j):
                current_set.add(synonyms[j][1])

        # If the current set is a subset of the essay set, update the minimum number of Rs and length
        if current_set.issubset(essay_set):
            current_rs = sum(1 for word in current_set if 'r' in word.lower())
            current_length = sum(len(word) for word in current_set)
            if current_rs < min_rs or (current_rs == min_rs and current_length < min_length):
                min_rs = current_rs
                min_length = current_length

    return min_rs, min_length

if __name__ == '__main__':
    m, essay = input().split()
    n = int(input())
    synonyms = [input().split() for _ in range(n)]
    min_rs, min_length = f1(m, essay, n, synonyms)
    print(min_rs, min_length)

