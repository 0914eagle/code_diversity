
def get_unique_names(names):
    unique_names = []
    for name in names:
        if name not in unique_names:
            unique_names.append(name)
    return unique_names

def get_repeated_names(names):
    repeated_names = []
    for name in names:
        if name in repeated_names:
            repeated_names.append(name)
    return repeated_names

def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())
    unique_names = get_unique_names(names)
    repeated_names = get_repeated_names(names)
    for name in unique_names:
        print("NO")
    for name in repeated_names:
        print("YES")

if __name__ == '__main__':
    main()

