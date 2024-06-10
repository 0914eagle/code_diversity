
def is_bored(S: str) -> int:
    def count_boredoms(sentences):
        count = 0
        for sentence in sentences:
            if sentence.strip().startswith("I"):
                count += 1
        return count

    def split_sentences(text):
        delimiters = ['.', '?', '!']
        for delimiter in delimiters:
            text = text.replace(delimiter, '|')
        return text.split('|')

    input_text = input().strip()
    sentences = split_sentences(input_text)
    boredom_count = count_boredoms(sentences)
    print(boredom_count)

is_bored(input())
