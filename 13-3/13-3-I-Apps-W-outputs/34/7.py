
def check_substring(word):
    # Check if the word is a substring of CODEFORCES
    if word in "CODEFORCES":
        return "YES"
    else:
        return "NO"

def main():
    word = input()
    print(check_substring(word))

if __name__ == '__main__':
    main()

