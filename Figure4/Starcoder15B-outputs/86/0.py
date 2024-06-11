def anti_shuffle(s):
    
    # Your code here
    # split string into words
    words = s.split()
    # loop through words
    for i in range(len(words)):
        # sort letters in each word
        words[i] = ''.join(sorted(words[i]))
    # join words back together
    return ' '.join(words)

#