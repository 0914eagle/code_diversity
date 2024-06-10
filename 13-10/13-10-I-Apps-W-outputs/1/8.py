
def get_alphabet_value(letter):
    return ord(letter) - ord('a') + 1

def get_name_from_number(k):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    name = ''
    while k > 0:
        name = alphabet[k-1] + name
        k -= get_alphabet_value(alphabet[k-1])
    return name

def get_shortest_name_from_number(k):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shortest_name = ''
    for letter in alphabet:
        name = letter + get_name_from_number(k-get_alphabet_value(letter))
        if len(name) < len(shortest_name) or (len(name) == len(shortest_name) and name < shortest_name):
            shortest_name = name
    return shortest_name

def main():
    k = int(input())
    print(get_shortest_name_from_number(k))

if __name__ == '__main__':
    main()

