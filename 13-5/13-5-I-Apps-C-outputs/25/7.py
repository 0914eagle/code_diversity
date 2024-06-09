
def get_key_presses(word):
    key_presses = []
    for char in word:
        key_presses.append(char)
    return key_presses

def get_optimal_key_presses(word, dictionary):
    optimal_key_presses = []
    for char in word:
        if char in dictionary:
            optimal_key_presses.append(char)
        else:
            optimal_key_presses.append("R")
    return optimal_key_presses

def main():
    N = int(input())
    dictionary = set()
    for i in range(N):
        word = input()
        dictionary.add(word)
    Q = int(input())
    for i in range(Q):
        word = input()
        key_presses = get_key_presses(word)
        optimal_key_presses = get_optimal_key_presses(word, dictionary)
        print("".join(optimal_key_presses))

if __name__ == '__main__':
    main()

