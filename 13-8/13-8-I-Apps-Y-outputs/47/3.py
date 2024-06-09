
def solve(string, k):
    n = len(string)
    for i in range(n):
        for j in range(i+1, min(n, i+k+1)):
            string = string[:i] + string[j] + string[i+1:j] + string[i] + string[j+1:]
    return string

