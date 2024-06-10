
def rearrange_letters(s):
    n = len(s)
    if n % 2 == 1 or n > 10000:
        return "-1"
    
    # split the string into pairs of letters
    pairs = [s[i:i+2] for i in range(0, n, 2)]
    
    # create a dictionary to store the counts of each letter
    letter_counts = {}
    for pair in pairs:
        for letter in pair:
            if letter not in letter_counts:
                letter_counts[letter] = 1
            else:
                letter_counts[letter] += 1
    
    # sort the letters by count in descending order
    sorted_letters = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)
    
    # create a new string with the sorted letters
    new_string = ""
    for letter, count in sorted_letters:
        new_string += letter * count
    
    # check if the new string has all unique substrings of length n/2
    substrings = [new_string[i:i+n//2] for i in range(n+1-n//2)]
    if len(set(substrings)) == n//2+1:
        return new_string
    else:
        return "-1"

def main():
    s = input("Enter a string of even length: ")
    print(rearrange_letters(s))

if __name__ == '__main__':
    main()

