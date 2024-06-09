
def f1(n, words):
    # Initialize a dictionary to store the words and their frequencies
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    # Return the sorted list of words and their frequencies
    return sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

def f2(n, words, queries):
    # Initialize an empty list to store the answers
    answers = []
    
    # Iterate over the queries
    for query in queries:
        # If the query is of the first type, append the word to the list of answers
        if query[0] == 1:
            answers.append(query[1])
        # If the query is of the second type, count the number of words that have the word on the stone tablet as a consecutive substring
        elif query[0] == 2:
            count = 0
            for word in words:
                if query[1] in word:
                    count += 1
            answers.append(count)
    
    # Return the list of answers
    return answers

if __name__ == '__main__':
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    q = int(input())
    queries = []
    for i in range(q):
        queries.append(list(map(int, input().split())))
    print(*f1(n, words), sep='\n')
    print(*f2(n, words, queries), sep='\n')

