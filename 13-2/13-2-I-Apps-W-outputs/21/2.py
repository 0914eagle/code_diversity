
def get_lexemes(command_line):
    lexemes = []
    current_lexeme = ""
    in_quotes = False
    for char in command_line:
        if char == " " and not in_quotes:
            if current_lexeme != "":
                lexemes.append(current_lexeme)
                current_lexeme = ""
        elif char == '"':
            in_quotes = not in_quotes
        else:
            current_lexeme += char
    if current_lexeme != "":
        lexemes.append(current_lexeme)
    return lexemes

