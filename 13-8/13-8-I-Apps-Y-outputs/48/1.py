
def get_correct_choice(a, b):
    choices = [1, 2, 3]
    wrong_choices = [a, b]
    correct_choice = list(set(choices) - set(wrong_choices))[0]
    return correct_choice

def main():
    a, b = map(int, input().split())
    print(get_correct_choice(a, b))

if __name__ == '__main__':
    main()

