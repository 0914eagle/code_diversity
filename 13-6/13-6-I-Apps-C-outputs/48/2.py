
def f1(N, words):
    # Initialize a dictionary to store the words and their frequencies
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    # Return the dictionary
    return word_freq

def f2(word_freq, S):
    # Initialize a variable to store the answer
    answer = 0

    # Iterate through the dictionary and check if the word is a substring of any of the other words
    for word, freq in word_freq.items():
        if S in word:
            answer += freq

    # Return the answer
    return answer

if __name__ == '__main__':
    N = int(input())
    words = []
    for i in range(N):
        words.append(input())
    Q = int(input())
    for i in range(Q):
        T = int(input())
        if T == 1:
            P = input()
            print(f1(N, words))
        else:
            S = int(input())
            print(f2(f1(N, words), S))

