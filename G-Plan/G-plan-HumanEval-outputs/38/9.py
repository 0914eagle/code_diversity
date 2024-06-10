
def remove_vowels(text: str) -> str:
    vowels = set('aeiouAEIOU')
    return ''.join([char for char in text if char not in vowels])

# Main function to read input and call the remove_vowels function
def main():
    text = input().strip()
    result = remove_vowels(text)
    print(result)

if __name__ == "__main__":
    main()
