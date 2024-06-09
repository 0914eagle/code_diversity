
def get_key_presses(word, dictionary):
    key_presses = []
    for char in word:
        if char in dictionary:
            key_presses.append(dictionary[char])
        else:
            key_presses.append("R")
    return key_presses

def get_optimal_key_presses(word, dictionary):
    key_presses = get_key_presses(word, dictionary)
    return "".join(key_presses)

def main():
    dictionary = {}
    N = int(input())
    for i in range(N):
        word = input()
        dictionary[word] = i + 1
    Q = int(input())
    for i in range(Q):
        word = input()
        print(get_optimal_key_presses(word, dictionary))

if __name__ == '__main__':
    main()

