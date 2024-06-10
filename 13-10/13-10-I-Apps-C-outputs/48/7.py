
def rearrange_letters(s):
    n = len(s)
    if n % 2 == 1 or n > 10000:
        return "-1"
    
    # create a list of all substrings of length n//2
    substrings = []
    for i in range(n - n//2 + 1):
        substrings.append(s[i:i+n//2])
    
    # check if all substrings are different
    for i in range(len(substrings)):
        for j in range(i+1, len(substrings)):
            if substrings[i] == substrings[j]:
                return "-1"
    
    # rearrrange the letters to form a new string
    new_string = ""
    for i in range(n//2):
        new_string += s[i]
        new_string += s[n-i-1]
    
    return new_string

def main():
    s = input()
    print(rearrange_letters(s))

if __name__ == '__main__':
    main()

