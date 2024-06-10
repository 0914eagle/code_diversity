
def find_hidden_strings(s):
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if s[i] == s[j]:
                count += 1
    return count

def find_secret_message(s):
    hidden_strings = []
    n = len(s)
    for i in range(n):
        for j in range(i+1, n):
            if s[i] == s[j]:
                hidden_strings.append(s[i:j+1])
    count = {}
    for hidden_string in hidden_strings:
        if hidden_string not in count:
            count[hidden_string] = 1
        else:
            count[hidden_string] += 1
    max_count = max(count.values())
    return [k for k, v in count.items() if v == max_count]

if __name__ == '__main__':
    s = input()
    print(find_hidden_strings(s))
    print(find_secret_message(s))

