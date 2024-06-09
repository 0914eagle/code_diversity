
def get_unique_names(names):
    unique_names = []
    for name in names:
        if name not in unique_names:
            unique_names.append(name)
    return unique_names

def get_presence_status(names):
    unique_names = get_unique_names(names)
    presence_status = []
    for name in names:
        if name in unique_names:
            presence_status.append("NO")
        else:
            presence_status.append("YES")
    return presence_status

def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())
    presence_status = get_presence_status(names)
    for status in presence_status:
        print(status)

if __name__ == '__main__':
    main()

