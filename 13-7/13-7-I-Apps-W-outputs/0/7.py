
def get_key(words, a):
    n = len(words)
    key = [chr(i + ord('a')) for i in range(n)]
    for i in range(n):
        word = words[i]
        for j in range(n):
            if word[j] != key[j]:
                key[j], key[word.index(key[j])] = key[word.index(key[j])], key[j]
                break
    if key == sorted(key):
        return "DA\n" + "".join(key)
    else:
        return "NE"

def main():
    n = int(input())
    words = [input() for _ in range(n)]
    a = [int(i) for i in input().split()]
    print(get_key(words, a))

if __name__ == '__main__':
    main()

