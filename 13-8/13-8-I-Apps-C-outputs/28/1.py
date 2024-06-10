
def hidden_strings(s):
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if s[i] == s[j] == s[k]:
                    count += 1
    return count

def secret_message(s):
    hidden_strings_count = hidden_strings(s)
    return hidden_strings_count

if __name__ == '__main__':
    s = input()
    print(secret_message(s))

