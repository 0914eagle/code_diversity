
def find_unique_substrings(strings, b):
    return len(set(b[i:j] for i in range(len(b)) for j in range(i+1, len(b)+1)))

