
def count_words_covered(words, patterns):
    def matches_pattern(word, pattern):
        if len(word) != len(pattern):
            return False
        for w, p in zip(word, pattern):
            if p != '*' and w != p:
                return False
        return True

    word_counts = []
    for pattern in patterns:
        count = 0
        for word in words:
            if matches_pattern(word, pattern):
                count += 1
        word_counts.append(count)
    return word_counts

if __name__ == "__main__":
    N, Q = map(int, input().split())
    words = [input().strip() for _ in range(N)]
    patterns = [input().strip() for _ in range(Q)]

    result = count_words_covered(words, patterns)
    for count in result:
        print(count)
