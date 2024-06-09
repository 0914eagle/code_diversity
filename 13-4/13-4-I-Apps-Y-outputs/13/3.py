
def get_lexicographically_min_string(string, k):
    n = len(string)
    for i in range(n-1):
        if string[i] > string[i+1] and k > 0:
            string = string[:i] + string[i+1] + string[i] + string[i+2:]
            k -= 1
    return string

q = int(input())
for i in range(q):
    n, k = map(int, input().split())
    string = input()
    print(get_lexicographically_min_string(string, k))

