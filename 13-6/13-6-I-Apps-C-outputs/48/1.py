
def f1(N, words):
    # Initialize a dictionary to store the words and their frequencies
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    # Sort the dictionary by value in descending order
    word_freq = dict(sorted(word_freq.items(), key=lambda item: item[1], reverse=True))
    
    # Return the top N words
    return list(word_freq.keys())[:N]

def f2(N, words, queries):
    # Initialize a dictionary to store the words and their frequencies
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    # Sort the dictionary by value in descending order
    word_freq = dict(sorted(word_freq.items(), key=lambda item: item[1], reverse=True))
    
    # Initialize a list to store the answers
    answers = []
    
    # Iterate over the queries
    for query in queries:
        # If the query is of type 1, add the word to the dictionary
        if query[0] == 1:
            word = query[1]
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
        
        # If the query is of type 2, find the frequency of the word on the stone tablet
        elif query[0] == 2:
            word = query[2]
            if word in word_freq:
                answers.append(word_freq[word])
            else:
                answers.append(0)
    
    # Return the answers
    return answers

if __name__ == '__main__':
    N = int(input())
    words = []
    for _ in range(N):
        words.append(input())
    Q = int(input())
    queries = []
    for _ in range(Q):
        queries.append(list(map(int, input().split())))
    top_N_words = f1(N, words)
    answers = f2(N, words, queries)
    for answer in answers:
        print(answer)

