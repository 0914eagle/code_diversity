
def encrypt(word, key):
    return ''.join(key[ord(c) - ord('a')] for c in word)

def solve(words, a):
    n = len(words)
    for key in permutations('abcdefghijklmnopqrstuvwxyz'):
        encrypted_words = [encrypt(word, key) for word in words]
        if sorted(encrypted_words) == [words[i-1] for i in a]:
            return 'DA\n' + ''.join(key)
    return 'NE'

if __name__ == '__main__':
    n = int(input())
    words = [input() for _ in range(n)]
    a = [int(i) for i in input().split()]
    print(solve(words, a))

