
def count_words_covered(words, patterns):
    def match_pattern(word, pattern):
        if len(word) != len(pattern):
            return False
        for w, p in zip(word, pattern):
            if p != '*' and w != p:
                return False
        return True

    word_dict = {}
    for word in words:
        for i in range(len(word) + 1):
            pattern = word[:i] + '*' + word[i + 1:]
            if pattern not in word_dict:
                word_dict[pattern] = 0
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

    for count in count_words_covered(words, patterns):
        print(count)
