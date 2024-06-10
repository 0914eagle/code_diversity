
def get_input():
    n, k = map(int, input().split())
    characters = []
    for _ in range(n):
        characters.append(list(map(int, input())))
    return n, k, characters

def get_character(characters):
    # Initialize the character with all features
    character = [1] * len(characters[0])
    
    # Loop through each feature and check if it is present in any of the other characters
    for i in range(len(characters[0])):
        for j in range(len(characters)):
            if characters[j][i] == 0:
                character[i] = 0
                break
    
    return character

def main():
    n, k, characters = get_input()
    character = get_character(characters)
    print(' '.join(map(str, character)))

if __name__ == '__main__':
    main()

