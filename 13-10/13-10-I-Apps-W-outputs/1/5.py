
def convert_to_number(name):
    value = 0
    for i in range(len(name)):
        value += abs(ord(name[i]) - ord(name[i-1]))
    return value

def find_shortest_name(k):
    for i in range(97, 123):
        for j in range(i+1, 123):
            name = chr(i) + chr(j)
            if convert_to_number(name) == k:
                return name
    return ""

def main():
    k = int(input())
    print(find_shortest_name(k))

if __name__ == '__main__':
    main()

