
def get_key(words, a):
    n = len(words)
    for key in permutations('abcdefghijklmnopqrstuvwxyz'):
        key = ''.join(key)
        encrypted_words = [word[i-1] for i in a]
        encrypted_words = [key[i-1] for i in encrypted_words]
        if sorted(encrypted_words) == words:
            return key
    return "NE"

def main():
    n = int(input())
    words = [input() for _ in range(n)]
    a = [int(i) for i in input().split()]
    print("DA")
    print(get_key(words, a))

if __name__ == '__main__':
    main()

