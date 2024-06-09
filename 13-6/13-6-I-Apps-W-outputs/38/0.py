
def get_unique_names(names):
    unique_names = []
    for name in names:
        if name not in unique_names:
            unique_names.append(name)
    return unique_names

def get_duplicate_names(names):
    unique_names = get_unique_names(names)
    duplicate_names = []
    for name in names:
        if name in unique_names:
            duplicate_names.append(name)
    return duplicate_names

def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())
    unique_names = get_unique_names(names)
    duplicate_names = get_duplicate_names(names)
    for name in unique_names:
        print("NO")
    for name in duplicate_names:
        print("YES")

if __name__ == '__main__':
    main()

