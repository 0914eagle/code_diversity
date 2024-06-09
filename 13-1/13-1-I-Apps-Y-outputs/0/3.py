
def rhyming_slang(common_word, ending_lists, phrases):
    # Initialize an empty list to store the results
    results = []
    
    # Iterate over the phrases
    for phrase in phrases:
        # Check if the last word of the phrase rhymes with the common word
        if phrase.split()[-1].endswith(common_word[-1]):
            # Check if the first word of the phrase is in the list of word endings that sound the same
            if phrase.split()[0][-1] in ending_lists[0]:
                # Check if the second word of the phrase is in the list of word endings that sound the same
                if len(phrase.split()) > 1 and phrase.split()[1][-1] in ending_lists[1]:
                    results.append("YES")
                else:
                    results.append("NO")
            else:
                results.append("NO")
        else:
            results.append("NO")
    
    return results

