
def is_bored(S: str) -> int:
    def count_boredoms(sentences):
        count = 0
        for sentence in sentences:
            if sentence.strip().startswith('I'):
                count += 1
        return count

    def split_sentences(S):
        delimiters = ['.', '?', '!']
        sentences = []
        current_sentence = ''
        for char in S:
            current_sentence += char
            if char in delimiters:
                sentences.append(current_sentence.strip())
                current_sentence = ''
        if current_sentence:
            sentences.append(current_sentence.strip())
        return sentences

    sentences = split_sentences(S)
    boredom_count = count_boredoms(sentences)
    return boredom_count

S = input()
print(is_bored(S))