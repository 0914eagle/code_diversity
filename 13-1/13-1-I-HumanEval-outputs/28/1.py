
def remove_vowels(text: str) -> str:
    
    vowels = set('aeiouAEIOU')
    return ''.join([char for char in text if char not in vowels])

