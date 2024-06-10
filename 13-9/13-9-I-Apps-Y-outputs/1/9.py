
def converse(characters):
    # Implement your solution here
    return ...

def main():
    num_characters = int(input())
    characters = []
    for i in range(num_characters):
        character = input()
        characters.append(character)
    print(converse(characters))

if __name__ == '__main__':
    main()

