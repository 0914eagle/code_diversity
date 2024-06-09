
def f1(n, letters):
    # Your code here
    return "DA" if is_winning_word(letters) else "NE"

def f2(n, letters):
    # Your code here
    return get_most_beautiful_word(letters)

def is_winning_word(letters):
    return any(letter == "a" for letter in letters)

def get_most_beautiful_word(letters):
    return "".join(sorted(letters))

if __name__ == '__main__':
    n = int(input())
    letters = input()
    print(f1(n, letters))
    print(f2(n, letters))

