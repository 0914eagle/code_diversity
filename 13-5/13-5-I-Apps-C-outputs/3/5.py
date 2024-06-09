
def get_pattern(files, delete_indices):
    pattern = ""
    for i in range(len(files[0])):
        char = files[0][i]
        if i in delete_indices:
            pattern += "?"
        else:
            pattern += char
    return pattern

def main():
    n, m = map(int, input().split())
    files = [input() for _ in range(n)]
    delete_indices = set(map(int, input().split()))
    pattern = get_pattern(files, delete_indices)
    print("Yes" if pattern else "No")
    if pattern:
        print(pattern)

if __name__ == '__main__':
    main()

