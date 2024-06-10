
def get_hidden_strings(s):
    hidden_strings = []
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                hidden_strings.append(s[i:j+1])
    return hidden_strings

def get_occurrences(hidden_strings):
    occurrences = {}
    for hidden_string in hidden_strings:
        if hidden_string not in occurrences:
            occurrences[hidden_string] = 1
        else:
            occurrences[hidden_string] += 1
    return occurrences

def get_max_occurrences(occurrences):
    max_occurrences = 0
    for hidden_string, count in occurrences.items():
        if count > max_occurrences:
            max_occurrences = count
    return max_occurrences

def get_secret_message(s):
    hidden_strings = get_hidden_strings(s)
    occurrences = get_occurrences(hidden_strings)
    max_occurrences = get_max_occurrences(occurrences)
    for hidden_string, count in occurrences.items():
        if count == max_occurrences:
            return hidden_string
    return ""

def main():
    s = input()
    print(get_secret_message(s))

if __name__ == '__main__':
    main()

