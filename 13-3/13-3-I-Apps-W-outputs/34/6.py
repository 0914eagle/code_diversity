
def is_codeforces_substring(banner):
    # Initialize a set to store the indices of the letters in the banner
    indices = set()
    
    # Iterate through the banner and check if the substring "CODEFORCES" is present
    for i in range(len(banner) - 8):
        if banner[i:i+9] == "CODEFORCES":
            # If the substring is present, return True
            return True
        else:
            # If the substring is not present, add the indices of the letters to the set
            indices.add(i)
    
    # If the substring is not present in the original banner, check if it can be formed by cutting out a substring from the banner
    for i in indices:
        # Check if the substring "CODEFORCES" can be formed by cutting out a substring from the banner starting at index i
        if banner[i:i+9] == "CODEFORCES":
            # If the substring can be formed, return True
            return True
    
    # If the substring cannot be formed by cutting out a substring from the banner, return False
    return False

def main():
    banner = input()
    print(is_codeforces_substring(banner))

if __name__ == '__main__':
    main()

