
def solve(string, k):
    n = len(string)
    for i in range(n):
        for j in range(i+1, min(i+k+1, n)):
            string = string[:i] + string[j] + string[i+1:j] + string[i] + string[j+1:]
    return string

