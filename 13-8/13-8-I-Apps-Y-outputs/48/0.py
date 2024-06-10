
def get_correct_choice(a, b):
    choices = [1, 2, 3]
    correct_choice = list(set(choices) - set([a, b]))[0]
    return correct_choice

def main():
    a, b = map(int, input().split())
    correct_choice = get_correct_choice(a, b)
    print(correct_choice)

if __name__ == '__main__':
    main()

