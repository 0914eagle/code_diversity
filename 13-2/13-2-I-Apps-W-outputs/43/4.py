
def solve(n, m, words, lecture):
    # Create a dictionary to map each word to its corresponding word in the other language
    word_map = {}
    for i in range(m):
        word_map[words[i][0]] = words[i][1]
        word_map[words[i][1]] = words[i][0]
    
    # Initialize an empty list to store the recorded lecture
    recorded_lecture = []
    
    # Iterate through the lecture text
    for word in lecture:
        # If the word is in the first language, add it to the recorded lecture
        if word in word_map:
            recorded_lecture.append(word)
        # If the word is in the second language, add its corresponding word in the first language to the recorded lecture
        else:
            recorded_lecture.append(word_map[word])
    
    return recorded_lecture

