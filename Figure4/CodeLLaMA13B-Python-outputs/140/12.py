def fix_spaces(text):
    
    if not text:
        return text
    new_text = text[0]
    for i in range(1, len(text)):
        if text[i] == ' ' and new_text[-1] == ' ':
            new_text += '-'
        elif text[i] == ' ' and new_text[-1] != ' ':
            new_text += '_'
        else:
            new_text += text[i]
    return new_text


if __name__ == '__main__':
    # These "asserts