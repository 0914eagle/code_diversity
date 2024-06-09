
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

def check_pattern(pattern, filenames, indices):
    for i in range(len(filenames)):
        if i in indices:
            if not filenames[i].startswith(pattern):
                return False
        else:
            if filenames[i].startswith(pattern):
                return False
    return True

def main():
    n, m = map(int, input().split())
    filenames = [input() for _ in range(n)]
    indices = set(map(int, input().split()))
    pattern = get_pattern(filenames, indices)
    if check_pattern(pattern, filenames, indices):
        print("Yes")
        print(pattern)
    else:
        print("No")

if __name__ == '__main__':
    main()

