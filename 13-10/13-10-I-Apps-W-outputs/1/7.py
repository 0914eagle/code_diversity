
def encode_number(k):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    name = ''
    while k > 0:
        name = alphabet[k-1] + name
        k = k // 26
    return name

def decode_name(name):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    value = 0
    for i in range(len(name)):
        value += abs(alphabet.index(name[i]) - alphabet.index(name[i-1]))
    return value

def get_shortest_name(k):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(alphabet)):
        name = alphabet[i]
        value = decode_name(name)
        if value == k:
            return name
    return None

def get_shortest_names(k):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    names = []
    for i in range(len(alphabet)):
        name = alphabet[i]
        value = decode_name(name)
        if value == k:
            names.append(name)
    return names

def get_name(k):
    names = get_shortest_names(k)
    if len(names) == 1:
        return names[0]
    else:
        return min(names)

if __name__ == '__main__':
    k = int(input())
    print(get_name(k))

