
def count_words_covered(words, patterns):
    word_dict = {}
    for word in words:
        for i in range(len(word) + 1):
            pattern = word[:i] + '*' + word[i:]
            if pattern not in word_dict:
                word_dict[pattern] = 1
            else:
                word_dict[pattern] += 1
    
    result = []
    for pattern in patterns:
        count = word_dict.get(pattern, 0)
        result.append(count)
    
    return result

if __name__ == "__main__":
    N, Q = map(int, input().split())
    words = [input().strip() for _ in range(N)]
    patterns = [input().strip() for _ in range(Q)]
    
    results = count_words_covered(words, patterns)
    for count in results:
        print(count)
