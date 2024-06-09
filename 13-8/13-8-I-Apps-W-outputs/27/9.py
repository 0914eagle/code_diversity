
def min_cards_to_verify_statement(s):
    vowels = set("aeiou")
    evens = set("02468")
    count = 0
    for i in range(len(s)):
        if s[i].isalpha() and s[i].lower() in vowels:
            if s[i-1].isdigit() and s[i-1] not in evens:
                count += 1
            if (i + 1) < len(s) and s[i+1].isdigit() and s[i+1] not in evens:
                count += 1
    return count

