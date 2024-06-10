
def encrypt(words, key):
    encrypted_words = []
    for word in words:
        encrypted_word = ""
        for char in word:
            encrypted_word += key[ord(char) - ord('a')]
        encrypted_words.append(encrypted_word)
    return encrypted_words

def solve(words, A):
    N = len(words)
    for key in permutations(ascii_lowercase):
        encrypted_words = encrypt(words, key)
        if encrypted_words == sorted(encrypted_words) == [words[i-1] for i in A]:
            return "DA", "".join(key)
    return "NE", ""

if __name__ == '__main__':
    N = int(input())
    words = [input() for _ in range(N)]
    A = [int(i) for i in input().split()]
    print(solve(words, A))

