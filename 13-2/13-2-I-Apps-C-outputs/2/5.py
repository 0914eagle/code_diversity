
def longest_common_prefix(word1, word2):
    for i in range(min(len(word1), len(word2))):
        if word1[i] != word2[i]:
            return word1[:i]
    return word1[:min(len(word1), len(word2))]

def algorithm_steps(query_word, database):
    steps = 0
    for word in database:
        steps += len(longest_common_prefix(query_word, word))
    return steps

if __name__ == '__main__':
    N = int(input())
    database = []
    for i in range(N):
        database.append(input())
    Q = int(input())
    for i in range(Q):
        query_word = input()
        print(algorithm_steps(query_word, database))

