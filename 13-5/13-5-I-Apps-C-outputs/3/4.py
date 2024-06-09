
def get_pattern(filenames, indices):
    pattern = ""
    for i in range(len(filenames[0])):
        count = 0
        for filename in filenames:
            if filename[i] != ".":
                count += 1
        if count == len(indices):
            pattern += "."
        elif count == 0:
            pattern += "?"
        else:
            return "No"
    return "Yes\n" + pattern

def main():
    n, m = map(int, input().split())
    filenames = [input() for _ in range(n)]
    indices = list(map(int, input().split()))
    print(get_pattern(filenames, indices))

if __name__ == '__main__':
    main()

