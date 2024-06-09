
def get_pattern(filenames):
    pattern = ""
    for filename in filenames:
        for i, char in enumerate(filename):
            if pattern[i] != char and pattern[i] != "?":
                pattern = pattern[:i] + "?" + pattern[i+1:]
                break
        else:
            continue
        break
    return pattern

def get_deleted_files(filenames, pattern):
    deleted_files = []
    for filename in filenames:
        if filename == pattern:
            deleted_files.append(filename)
    return deleted_files

def main():
    n, m = map(int, input().split())
    filenames = []
    for _ in range(n):
        filenames.append(input())
    indices = list(map(int, input().split()))
    pattern = get_pattern(filenames)
    deleted_files = get_deleted_files(filenames, pattern)
    if len(deleted_files) == m:
        print("Yes")
        print(pattern)
    else:
        print("No")

if __name__ == '__main__':
    main()

