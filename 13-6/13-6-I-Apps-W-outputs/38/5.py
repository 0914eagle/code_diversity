
def check_presence(names, name):
    for i in range(len(names)):
        if names[i] == name:
            return "YES"
    return "NO"

def main():
    n = int(input())
    names = []
    for i in range(n):
        name = input()
        names.append(name)
        print(check_presence(names, name))

if __name__ == '__main__':
    main()

