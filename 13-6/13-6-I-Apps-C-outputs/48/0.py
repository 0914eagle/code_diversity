
def count_substring(word, substring):
    count = 0
    for i in range(len(word)):
        if word[i:i+len(substring)] == substring:
            count += 1
    return count

def f1(N, words):
    return [word for word in words]

def f2(N, words, S):
    return count_substring(words[S-1], words[S-1])

if __name__ == '__main__':
    N = int(input())
    words = [input() for _ in range(N)]
    Q = int(input())
    for _ in range(Q):
        T, P = map(int, input().split())
        if T == 1:
            print(f1(N, P))
        else:
            print(f2(N, words, S))

