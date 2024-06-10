
def is_bored(S: str) -> int:
    def count_boredoms(sentences):
        count = 0
        for sentence in sentences:
            if sentence.startswith('I'):
                count += 1
        return count

    def split_into_sentences(S):
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

    input_string = S
    sentences = split_into_sentences(input_string)
    boredom_count = count_boredoms(sentences)
    return boredom_count

input_string = input()
print(is_bored(input_string))
