
import re

def generate_grammar(rules):
    grammar = {}
    for rule in rules:
        variable, production = rule.split(" -> ")
        grammar[variable] = production
    return grammar

def search_text(text, grammar):
    matches = []
    for line in text:
        longest_match = ""
        for variable in grammar:
            pattern = re.compile(f"{variable}")
            match = pattern.search(line)
            if match:
                longest_match = max(longest_match, match.group(), key=len)
        matches.append(longest_match)
    return matches

def main():
    rules = [input() for _ in range(int(input()))]
    grammar = generate_grammar(rules)
    text = [input() for _ in range(int(input()))]
    matches = search_text(text, grammar)
    for match in matches:
        print(match)

if __name__ == '__main__':
    main()

