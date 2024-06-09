
def is_present(name, names):
    return any(name == n for n in names)

def get_names(n):
    names = []
    for i in range(n):
        name = input()
        if is_present(name, names):
            print("YES")
        else:
            print("NO")
            names.append(name)
    return names

def main():
    n = int(input())
    get_names(n)

if __name__ == '__main__':
    main()

