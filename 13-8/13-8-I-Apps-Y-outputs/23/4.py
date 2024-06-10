
def get_kth_substring(s, k):
    substrings = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substrings.append(s[i:j])
    substrings.sort()
    return substrings[k-1]

def main():
    s = input("Enter a string: ")
    k = int(input("Enter the value of K: "))
    print(get_kth_substring(s, k))

if __name__ == '__main__':
    main()

