
def remove_vowels(text: str) -> str:
    vowels = set('aeiouAEIOU')
    return ''.join([char for char in text if char not in vowels])

# Main function to read input and test the remove_vowels function
if __name__ == "__main__":
    text = input().strip()
    result = remove_vowels(text)
    print(result)
