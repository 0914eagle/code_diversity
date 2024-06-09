
def hash_function(word, mod):
    if word == "":
        return 0
    else:
        return (hash_function(word[:-1], mod) * 33) ^ ord(word[-1]) % mod

def count_words(N, K, M):
    mod = 2**M
    count = 0
    for word in itertools.product(string.ascii_lowercase, repeat=N):
        if hash_function("".join(word), mod) == K:
            count += 1
    return count
