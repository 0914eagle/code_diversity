
def find_correct_choice(a, b):
    choices = [1, 2, 3]
    correct_choice = None
    for choice in choices:
        if choice not in [a, b]:
            correct_choice = choice
            break
    return correct_choice

def main():
    a = int(input())
    b = int(input())
    correct_choice = find_correct_choice(a, b)
    print(correct_choice)

if __name__ == '__main__':
    main()

