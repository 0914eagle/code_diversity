
def encrypt(word, key):
    return ''.join(key[ord(c) - ord('a')] for c in word)

def solve(words, arr):
    for key in permutations('abcdefghijklmnopqrstuvwxyz'):
        encrypted_words = [encrypt(word, key) for word in words]
        if encrypted_words == sorted(encrypted_words) == list(map(str, arr)):
            return 'DA\n' + ''.join(key)
    return 'NE'

if __name__ == '__main__':
    n = int(input())
    words = [input() for _ in range(n)]
    arr = [int(i) for i in input().split()]
    print(solve(words, arr))

