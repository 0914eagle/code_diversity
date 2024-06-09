
def get_previous_names(names):
    previous_names = set()
    for name in names:
        if name in previous_names:
            yield "YES"
        else:
            yield "NO"
        previous_names.add(name)

def main():
    n = int(input())
    names = [input() for _ in range(n)]
    for name in get_previous_names(names):
        print(name)

if __name__ == '__main__':
    main()

