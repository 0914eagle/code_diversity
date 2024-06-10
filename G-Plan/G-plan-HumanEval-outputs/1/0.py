
def is_bored(S: str) -> int:
    def count_boredoms(sentence: str) -> int:
        return 1 if sentence.strip().startswith('I') else 0

    def split_sentences(input_string: str) -> list:
        delimiters = ['.', '?', '!']
        sentences = []
        current_sentence = ''
        for char in input_string:
            current_sentence += char
            if char in delimiters:
                sentences.append(current_sentence.strip())
                current_sentence = ''
        if current_sentence:
            sentences.append(current_sentence.strip())
        return sentences

    total_boredoms = 0
    sentences = split_sentences(S)
    for sentence in sentences:
        total_boredoms += count_boredoms(sentence)
    
    return total_boredoms

input_string = input()
print(is_bored(input_string))
