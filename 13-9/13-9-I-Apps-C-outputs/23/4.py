
def is_same_word(word1, word2):
    if word1 == word2:
        return True
    if len(word1) == 0 or len(word2) == 0:
        return False
    if word1[-1] == word2[-1]:
        return is_same_word(word1[:-1], word2[:-1])
    return False

def is_consistent(statements):
    # Create a dictionary to store the relationships between words
    word_dict = {}
    for statement in statements:
        words = statement.split()
        if len(words) == 1:
            # If the statement is just one word, add it to the dictionary with itself as its rhyme
            word_dict[words[0]] = words[0]
        else:
            # If the statement is in the form "word1 is word2", add the relationship to the dictionary
            word1, word2 = words
            word_dict[word1] = word2
            word_dict[word2] = word1
    
    # Check if there are any contradictions in the dictionary
    for word1, word2 in word_dict.items():
        if word1 != word2 and not is_same_word(word1, word2):
            return "wait what?"
    
    return "yes"

def main():
    num_statements = int(input())
    statements = []
    for _ in range(num_statements):
        statements.append(input())
    print(is_consistent(statements))

if __name__ == '__main__':
    main()

