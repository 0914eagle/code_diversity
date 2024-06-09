
def get_original_string(strings):
    n = len(strings[0])
    for i in range(n):
        for j in range(i+1, n):
            if all(string[i] + string[j] in strings[k] for k in range(len(strings)) for string in strings):
                return ''.join(sorted(set(strings[0])))
    return -1

def main():
    k, n = map(int, input().split())
    strings = [input() for _ in range(k)]
    print(get_original_string(strings))

if __name__ == '__main__':
    main()

