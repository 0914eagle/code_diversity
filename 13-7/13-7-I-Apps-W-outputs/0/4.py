
def encrypt(word, key):
    return ''.join(key[ord(c) - ord('a')] for c in word)

def decrypt(word, key):
    return ''.join(chr(ord('a') + key.index(c)) for c in word)

def solve(words, a):
    for key in permutations('abcdefghijklmnopqrstuvwxyz'):
        encrypted_words = [encrypt(word, key) for word in words]
        sorted_words = sorted(encrypted_words)
        if sorted_words == a:
            return 'DA', ''.join(key)
    return 'NE', ''

if __name__ == '__main__':
    n = int(input())
    words = [input() for _ in range(n)]
    a = [int(i) for i in input().split()]
    result = solve(words, a)
    print(result[0])
    if result[0] == 'DA':
        print(result[1])

