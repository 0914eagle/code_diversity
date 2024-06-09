
import re

def generate_grammar(rules):
    grammar = {}
    for rule in rules:
        variable, production = rule.split(" -> ")
        grammar[variable] = production
    return grammar

def generate_strings(grammar, start_variable):
    strings = []
    for variable in grammar:
        if variable == start_variable:
            strings.append(grammar[variable])
        else:
            for production in grammar[variable]:
                strings.append(production + grammar[variable])
    return strings

def search_text(text, grammar, start_variable):
    strings = generate_strings(grammar, start_variable)
    for string in strings:
        if re.search(string, text):
            return string
    return "NONE"

def main():
    rules = input().split()
    grammar = generate_grammar(rules)
    start_variable = input()
    text = input()
    print(search_text(text, grammar, start_variable))

if __name__ == '__main__':
    main()

