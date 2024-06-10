
def get_correct_choice(a, b):
    # Convert the input to a set to remove duplicates
    choices = set([a, b])
    # Find the only element in the set that is not 1 or 2
    correct_choice = [x for x in choices if x not in [1, 2]][0]
    return correct_choice

def main():
    a, b = map(int, input().split())
    print(get_correct_choice(a, b))

if __name__ == '__main__':
    main()

