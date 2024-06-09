
def get_pattern(filenames, indices):
    pattern = ""
    for i in range(len(filenames[0])):
        count = 0
        for filename in filenames:
            if filename[i] == ".":
                count += 1
        if count == len(indices):
            pattern += "."
        else:
            pattern += "?"
    return pattern

def main():
    n, m = map(int, input().split())
    filenames = [input() for _ in range(n)]
    indices = list(map(int, input().split()))
    pattern = get_pattern(filenames, indices)
    print("Yes" if pattern else "No")
    if pattern:
        print(pattern)

if __name__ == '__main__':
    main()

