
def assign_value_to_letters(string):
    value = 0
    for char in string:
        value += abs(ord(char) - ord('a') + 1)
    return value

def find_shortest_string(k):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(alphabet)):
        for j in range(i+1, len(alphabet)):
            string = alphabet[i] + alphabet[j]
            if assign_value_to_letters(string) == k:
                return string
    return ''

def main():
    k = int(input())
    print(find_shortest_string(k))

if __name__ == '__main__':
    main()

