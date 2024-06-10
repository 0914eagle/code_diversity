
def get_input():
    n, k = map(int, input().split())
    characters = []
    for _ in range(n):
        characters.append(list(map(int, input().strip())))
    return n, k, characters

def get_character(characters, k):
    # Initialize the character with all features set to 0
    character = [0] * k
    
    # Iterate through the characters and find the features that are not present in any of them
    for c in characters:
        for i in range(k):
            if c[i] == 1 and character[i] == 0:
                character[i] = 1
    
    return character

def main():
    n, k, characters = get_input()
    character = get_character(characters, k)
    print(*character, sep='')

if __name__ == '__main__':
    main()

