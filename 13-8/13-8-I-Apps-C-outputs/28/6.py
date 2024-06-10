
def hidden_strings(s):
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if s[i] == s[j]:
                count += 1
    return count

def secret_message(s):
    hidden_strings_list = []
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                hidden_strings_list.append(s[i:j+1])
    hidden_strings_list = list(set(hidden_strings_list))
    count = 0
    for hidden_string in hidden_strings_list:
        count += hidden_strings(hidden_string)
    return count

if __name__ == '__main__':
    s = input()
    print(secret_message(s))

