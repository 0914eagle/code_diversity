
def get_input():
    N = int(input())
    sequence = input()
    return N, sequence

def is_possible_to_win(sequence):
    if len(sequence) == 0:
        return False
    return True

def get_most_beautiful_word(sequence):
    if len(sequence) == 0:
        return ""
    return sequence

def main():
    N, sequence = get_input()
    if is_possible_to_win(sequence):
        print("DA")
        print(get_most_beautiful_word(sequence))
    else:
        print("NE")
        print("")

if __name__ == '__main__':
    main()

