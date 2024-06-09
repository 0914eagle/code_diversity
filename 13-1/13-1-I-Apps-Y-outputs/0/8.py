
def rhyming_slang(common_word, ending_lists, phrases):
    # Initialize an empty list to store the results
    results = []
    
    # Iterate over the phrases
    for phrase in phrases:
        # Check if the last word of the phrase rhymes with the common word
        if phrase.split()[-1].endswith(common_word[-1]):
            # Check if the first word of the phrase is in any of the ending lists
            if any(phrase.split()[0].endswith(ending) for ending in ending_lists):
                # If both conditions are met, the phrase is a rhyming slang
                results.append("YES")
            else:
                # If the first word is not in any of the ending lists, the phrase is not a rhyming slang
                results.append("NO")
        else:
            # If the last word of the phrase does not rhyme with the common word, the phrase is not a rhyming slang
            results.append("NO")
    
    return results

