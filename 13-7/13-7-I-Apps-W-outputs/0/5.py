
def encrypt_and_sort(words, key):
    encrypted_words = []
    for word in words:
        encrypted_word = ""
        for char in word:
            encrypted_word += key[ord(char) - ord('a')]
        encrypted_words.append(encrypted_word)
    return sorted(encrypted_words)

def find_key(words, array):
    for key in permutations(string.ascii_lowercase):
        encrypted_words = encrypt_and_sort(words, key)
        if encrypted_words == array:
            return key
    return "NE"

if __name__ == '__main__':
    N = int(input())
    words = []
    for _ in range(N):
        words.append(input())
    array = list(map(int, input().split()))
    key = find_key(words, array)
    print("DA" if key != "NE" else "NE")
    if key != "NE":
        print("".join(key))

