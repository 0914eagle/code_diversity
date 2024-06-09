
def f1(N, words):
    # Initialize a dictionary to store the words and their frequencies
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    # Return the sorted list of words and their frequencies
    return sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

def f2(N, words, shown_word):
    # Initialize a counter to keep track of the number of words that contain the shown word as a substring
    count = 0
    for word in words:
        if shown_word in word:
            count += 1
    
    # Return the number of words that contain the shown word as a substring
    return count

if __name__ == '__main__':
    N = int(input())
    words = []
    for _ in range(N):
        words.append(input())
    Q = int(input())
    for _ in range(Q):
        T = int(input())
        if T == 1:
            shown_word = input()
            print(f1(N, words))
        else:
            S = int(input())
            print(f2(N, words, shown_word))

