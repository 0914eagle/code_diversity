
def get_cards(x, y):
    if x == 0 and y == 0:
        return "Impossible"
    if x == 1 and y == 1:
        return "AB"
    if x == 1 and y > 1:
        return "A" + get_cards(x, y-1)
    if y == 1 and x > 1:
        return "B" + get_cards(x-1, y)
    if x > 1 and y > 1:
        return "AB" + get_cards(x-1, y-1)

def get_compressed_string(string):
    compressed_string = ""
    count = 1
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            count += 1
        else:
            compressed_string += str(count) + string[i]
            count = 1
    compressed_string += str(count) + string[-1]
    return compressed_string

def main():
    x, y = map(int, input().split())
    string = get_cards(x, y)
    compressed_string = get_compressed_string(string)
    print(compressed_string)

if __name__ == '__main__':
    main()

