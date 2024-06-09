
def is_name_in_stream(name, stream):
    for i in range(len(stream)):
        if stream[i] == name:
            return "YES"
    return "NO"

def main():
    n = int(input())
    stream = []
    for i in range(n):
        name = input()
        stream.append(name)
        print(is_name_in_stream(name, stream))

if __name__ == '__main__':
    main()

