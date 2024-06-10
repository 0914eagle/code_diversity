
def get_input():
    return input().split()

def get_correct_choice(choices):
    return [choice for choice in choices if choice not in choices][0]

def main():
    choices = get_input()
    print(get_correct_choice(choices))

if __name__ == '__main__':
    main()

