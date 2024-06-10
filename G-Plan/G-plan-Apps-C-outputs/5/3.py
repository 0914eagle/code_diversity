
def preprocess_words(words):
    patterns_dict = {}
    for word in words:
        for i in range(len(word)+1):
            pattern = word[:i] + '*' + word[i+1:]
            if pattern in patterns_dict:
                patterns_dict[pattern].append(word)
            else:
                patterns_dict[pattern] = [word]
    return patterns_dict

def count_words_covered(patterns, patterns_dict):
    counts = []
    for pattern in patterns:
        count = patterns_dict.get(pattern, [])
        counts.append(len(count))
    return counts

if __name__ == "__main__":
    N, Q = map(int, input().split())
    words = [input().strip() for _ in range(N)]
    patterns = [input().strip() for _ in range(Q)]

    patterns_dict = preprocess_words(words)
    counts = count_words_covered(patterns, patterns_dict)

    for count in counts:
        print(count)
