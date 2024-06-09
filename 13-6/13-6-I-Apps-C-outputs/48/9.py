
def f1(n, words):
    return len(set(words))

def f2(n, words, s):
    return words.count(words[s-1])

if __name__ == '__main__':
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    q = int(input())
    for i in range(q):
        t = int(input())
        if t == 1:
            p = input()
            print(f1(n, words))
        else:
            s = int(input())
            print(f2(n, words, s))

