
def get_pattern(filenames, indices):
    pattern = ""
    for i in range(len(filenames[0])):
        char = filenames[0][i]
        for filename in filenames:
            if filename[i] != char and char != "?":
                return "No"
        if char == "?":
            pattern += "?"
        else:
            pattern += char
    return pattern

def main():
    n, m = map(int, input().split())
    filenames = [input() for _ in range(n)]
    indices = list(map(int, input().split()))
    pattern = get_pattern(filenames, indices)
    print("Yes" if pattern != "No" else "No")
    if pattern != "No":
        print(pattern)

if __name__ == '__main__':
    main()

