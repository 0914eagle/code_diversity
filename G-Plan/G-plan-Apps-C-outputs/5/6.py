
def count_words_covered(words, patterns):
    def generate_pattern(word):
        patterns = set()
        for i in range(len(word) + 1):
            patterns.add(word[:i] + '*' + word[i:])
        return patterns

    word_patterns = {}
    for word in words:
        patterns = generate_pattern(word)
        for pattern in patterns:
            if pattern in word_patterns:
                word_patterns[pattern].add(word)
            else:
                word_patterns[pattern] = {word}

    result = []
    for pattern in patterns:
        count = sum(1 for word in words if word in word_patterns.get(pattern, set()))
        result.append(count)

    return result

if __name__ == "__main__":
    N, Q = map(int, input().split())
    words = [input().strip() for _ in range(N)]
    patterns = [input().strip() for _ in range(Q)]

    result = count_words_covered(words, patterns)
    for count in result:
        print(count)
