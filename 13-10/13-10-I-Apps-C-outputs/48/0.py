
def rearrange_letters(s):
    n = len(s)
    if n % 2 == 1 or n > 10000:
        return "-1"
    
    # create a list of all possible substrings of length n//2
    substrings = []
    for i in range(n - n//2 + 1):
        substrings.append(s[i:i+n//2])
    
    # check if all substrings are unique
    if len(set(substrings)) == len(substrings):
        return s
    
    # if not, rearrange the letters to make all substrings unique
    substring_count = {}
    for substring in substrings:
        if substring not in substring_count:
            substring_count[substring] = 1
        else:
            substring_count[substring] += 1
    
    # sort the substring count dictionary by value in descending order
    substring_count = sorted(substring_count.items(), key=lambda x: x[1], reverse=True)
    
    # create a new string by rearranging the letters
    new_string = ""
    for substring, count in substring_count:
        new_string += substring
    
    return new_string

def main():
    s = input("Enter a string of even length between 2 and 10000: ")
    result = rearrange_letters(s)
    print(result)

if __name__ == '__main__':
    main()

