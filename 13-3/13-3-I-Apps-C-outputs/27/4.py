
def hash_function(word, mod):
    if word == "":
        return 0
    else:
        return (hash_function(word[:-1], mod) * 33) ^ ord(word[-1]) % mod

def count_words(N, K, M):
    count = 0
    for i in range(1, N+1):
        for word in itertools.product(string.ascii_lowercase, repeat=i):
            if hash_function("".join(word), 2**M) == K:
                count += 1
    return count

