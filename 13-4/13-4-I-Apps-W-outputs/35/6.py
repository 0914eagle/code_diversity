
def largest_swap_free_set(words):
    # Initialize a set to store the swap-free set
    swap_free_set = set()

    # Iterate over the words
    for word in words:
        # Check if the word is already in the swap-free set
        if word not in swap_free_set:
            # If not, add it to the swap-free set
            swap_free_set.add(word)
            # Iterate over the remaining words
            for other_word in words:
                # Check if the other word is already in the swap-free set
                if other_word not in swap_free_set:
                    # If not, check if the two words are swap-free
                    if are_swap_free(word, other_word):
                        # If they are, add the other word to the swap-free set
                        swap_free_set.add(other_word)

    # Return the size of the swap-free set
    return len(swap_free_set)

def are_swap_free(word1, word2):
    # Initialize a boolean to store the result
    result = True

    # Iterate over the letters in the first word
    for i in range(len(word1)):
        # Check if the letter at the current index is different in the second word
        if word1[i] != word2[i]:
            # If it is, check if there is another letter that is different in the second word
            for j in range(len(word2)):
                # If there is, return False
                if i != j and word1[i] != word2[j] and word1[j] != word2[i]:
                    result = False
                    break

    # Return the result
    return result

