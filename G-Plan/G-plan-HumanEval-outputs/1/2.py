
def is_bored(S: str) -> int:
    def count_boredoms(sentences):
        count = 0
        for sentence in sentences:
            if sentence.strip().startswith('I'):
                count += 1
        return count

    def split_sentences(S):
        delimiters = ['.', '?', '!']
        for delimiter in delimiters:
            S = S.replace(delimiter, '|')
        return S.split('|')

    sentences = split_sentences(S)
    boredom_count = count_boredoms(sentences)
    return boredom_count

S = input()
print(is_bored(S))
