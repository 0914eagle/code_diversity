
def f(string, k, m):
    # Apply f to the string k times
    for i in range(k):
        string = apply_f(string)
    # Return the mth character of the string
    return string[m-1]

def apply_f(string):
    # Convert each character to its corresponding string from the table
    table = {"a": "bc", "b": "cd", "c": "da", "d": "dd", "e": "ee", "f": "ff", "g": "gg", "h": "hh", "i": "ii", "j": "jj", "k": "kk", "l": "ll", "m": "mm", "n": "nn", "o": "oo", "p": "pp", "q": "qq", "r": "rr", "s": "ss", "t": "tt", "u": "uu", "v": "vv", "w": "ww", "x": "xx", "y": "yy", "z": "zz"}
    result = ""
    for char in string:
        result += table[char]
    return result

if __name__ == '__main__':
    S = input()
    T = input().split()
    K = int(input())
    M = int(input())
    m = list(map(int, input().split()))
    for i in range(M):
        print(f(S, K, m[i]))

