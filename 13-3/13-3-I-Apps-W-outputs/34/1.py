
def check_substring(word):
    # Check if the word is a substring of CODEFORCES
    if word in "CODEFORCES":
        return "YES"
    else:
        return "NO"

def check_substring_recursive(word):
    # Check if the word is a substring of CODEFORCES
    if word in "CODEFORCES":
        return "YES"
    
    # Check if the word can be obtained by removing the first letter of CODEFORCES
    if word[:-1] in "CODEFORCES":
        return "YES"
    
    # Check if the word can be obtained by removing the last letter of CODEFORCES
    if word[1:] in "CODEFORCES":
        return "YES"
    
    # Check if the word can be obtained by removing the first and last letter of CODEFORCES
    if word[1:-1] in "CODEFORCES":
        return "YES"
    
    # If none of the above conditions are met, return "NO"
    return "NO"

def main():
    word = input()
    print(check_substring_recursive(word))

if __name__ == '__main__':
    main()

