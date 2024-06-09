
def largest_swap_free_set(words):
    # Initialize a set to store the swap-free set
    swap_free_set = set()
    # Iterate through each word in the input list
    for word in words:
        # Check if the word is already in the swap-free set
        if word not in swap_free_set:
            # If not, add it to the set and check if it can be transformed into any other word in the set by swapping a single pair of letters
            swap_free_set.add(word)
            for other_word in swap_free_set:
                if can_swap_to_form_other_word(word, other_word):
                    # If it can be transformed into another word, remove the current word from the set
                    swap_free_set.remove(word)
                    break
    # Return the size of the largest swap-free set
    return len(swap_free_set)

def can_swap_to_form_other_word(word, other_word):
    # Initialize a boolean variable to store the result
    can_swap = False
    # Iterate through each letter in the word
    for i in range(len(word)):
        # Check if the letter at the current index is different from the corresponding letter in the other word
        if word[i] != other_word[i]:
            # If it is, check if the letter at the current index is also different from the corresponding letter in the other word
            if word[i] == other_word[i-1] or word[i] == other_word[i+1]:
                # If it is, return True
                can_swap = True
                break
    # Return the result
    return can_swap

