
def get_hidden_strings(s):
    hidden_strings = []
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                hidden_strings.append(s[i:j+1])
    return hidden_strings

def get_occurrences(s, hidden_strings):
    occurrences = {}
    for hidden_string in hidden_strings:
        indices = []
        for i in range(len(s)):
            if hidden_string == s[i:i+len(hidden_string)]:
                indices.append(i+1)
        if indices:
            occurrences[hidden_string] = indices
    return occurrences

def get_max_occurrences(occurrences):
    max_occurrences = 0
    for hidden_string, indices in occurrences.items():
        if len(indices) > max_occurrences:
            max_occurrences = len(indices)
    return max_occurrences

def main():
    s = input()
    hidden_strings = get_hidden_strings(s)
    occurrences = get_occurrences(s, hidden_strings)
    max_occurrences = get_max_occurrences(occurrences)
    print(max_occurrences)

if __name__ == '__main__':
    main()

