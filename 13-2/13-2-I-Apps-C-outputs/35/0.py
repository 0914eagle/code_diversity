
import re

def generate_grammar(rules):
    grammar = {}
    for rule in rules:
        head, production = rule.split(" -> ")
        grammar[head] = production
    return grammar

def generate_strings(grammar, start_variable):
    strings = []
    for variable in grammar:
        if variable == start_variable:
            strings.append(grammar[variable])
        else:
            for production in grammar[variable]:
                strings.append(production)
    return strings

def search_text(text, grammar, start_variable):
    strings = generate_strings(grammar, start_variable)
    for string in strings:
        if re.search(string, text):
            return string
    return "NONE"

def main():
    rules = []
    while True:
        try:
            line = input()
            if line == "":
                break
            rules.append(line)
        except EOFError:
            break
    grammar = generate_grammar(rules)
    start_variable = rules[0].split(" -> ")[0]
    while True:
        try:
            line = input()
            if line == "":
                break
            print(search_text(line, grammar, start_variable))
        except EOFError:
            break

if __name__ == '__main__':
    main()

