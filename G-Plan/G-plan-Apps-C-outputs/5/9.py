
def count_words_covered(words, patterns):
    word_dict = {}
    for word in words:
        for i in range(len(word)+1):
            pattern = word[:i] + '*' + word[i:]
            if pattern not in word_dict:
                word_dict[pattern] = 1
            else:
                word_dict[pattern] += 1
    
    result = []
    for pattern in patterns:
        if pattern in word_dict:
            result.append(word_dict[pattern])
        else:
            result.append(0)
    
    return result

if __name__ == "__main__":
    N, Q = map(int, input().split())
    words = [input().strip() for _ in range(N)]
    patterns = [input().strip() for _ in range(Q)]
    
    output = count_words_covered(words, patterns)
    for count in output:
        print(count)
