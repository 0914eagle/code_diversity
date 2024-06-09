
def get_lexicographically_min_string(string, k):
    n = len(string)
    for i in range(n):
        for j in range(i+1, min(i+k+1, n)):
            if string[i] > string[j]:
                string = string[:i] + string[j] + string[i+1:j] + string[i] + string[j+1:]
                k -= 1
                if k == 0:
                    return string
    return string

