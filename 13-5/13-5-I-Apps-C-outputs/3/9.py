
def get_pattern(filenames, indices):
    pattern = ""
    for i in range(len(filenames[0])):
        char = filenames[0][i]
        for j in range(1, len(filenames)):
            if filenames[j][i] != char:
                char = "?"
                break
        pattern += char
    return pattern

def get_deletable_files(filenames, pattern):
    deletable_files = []
    for filename in filenames:
        if filename == pattern:
            deletable_files.append(filename)
    return deletable_files

def main():
    n, m = map(int, input().split())
    filenames = [input() for _ in range(n)]
    indices = [int(i) for i in input().split()]
    pattern = get_pattern(filenames, indices)
    deletable_files = get_deletable_files(filenames, pattern)
    if len(deletable_files) == m:
        print("Yes")
        print(pattern)
    else:
        print("No")

if __name__ == '__main__':
    main()

