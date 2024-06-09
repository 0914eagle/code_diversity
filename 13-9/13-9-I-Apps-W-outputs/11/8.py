
def solve(k):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    min_length = float('inf')
    result = ''
    for i in range(len(alphabet)):
        for j in range(i+1, len(alphabet)):
            name = alphabet[i] + alphabet[j]
            value = abs(alphabet.index(name[0]) - alphabet.index(name[1]))
            if value == k and len(name) < min_length:
                min_length = len(name)
                result = name
    return result

