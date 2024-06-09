
def hash_function(word, mod):
    if word == "":
        return 0
    else:
        return (hash_function(word[:-1], mod) * 33) ^ ord(word[-1]) % mod

def count_words(n, k, m):
    mod = 2**m
    count = 0
    for i in range(26**n):
        word = chr(i + 97) * n
        if hash_function(word, mod) == k:
            count += 1
    return count

