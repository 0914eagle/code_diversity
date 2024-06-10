
def is_double_substring(s):
    count = 0
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                count += 1
    return count == 2

def main():
    s = input("Enter a 4-character string: ")
    if is_double_substring(s):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

