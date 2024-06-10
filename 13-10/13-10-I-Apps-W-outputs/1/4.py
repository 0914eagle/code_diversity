
def get_value(string):
    value = 0
    for i in range(len(string) - 1):
        value += abs(ord(string[i]) - ord(string[i + 1]))
    return value

def get_nametag(k):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(alphabet)):
        for j in range(i + 1, len(alphabet)):
            string = alphabet[i] + alphabet[j]
            if get_value(string) == k:
                return string
    return ""

def main():
    k = int(input())
    print(get_nametag(k))

if __name__ == '__main__':
    main()

