
def count_substring(string, substring):
    count = 0
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            count += 1
    return count

def f1(barbarians, word):
    return [count_substring(barbarians[i], word) for i in range(len(barbarians))]

def f2(barbarians, barbarian_index):
    return count_substring(barbarians[barbarian_index], barbarians[barbarian_index])

if __name__ == '__main__':
    N = int(input())
    barbarians = [input() for _ in range(N)]
    Q = int(input())
    for _ in range(Q):
        T = int(input())
        if T == 1:
            word = input()
            print(*f1(barbarians, word))
        else:
            barbarian_index = int(input())
            print(f2(barbarians, barbarian_index))

