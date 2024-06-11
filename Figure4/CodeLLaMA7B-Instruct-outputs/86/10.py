

def anti_shuffle(s):
    
    # Split the string into a list of words
    words = s.split()
    # Loop through each word and sort the characters
    for i in range(len(words)):
        words[i] = ''.join(sorted(words[i]))
    # Join the sorted words back into a string
    return ' '.join(words)


