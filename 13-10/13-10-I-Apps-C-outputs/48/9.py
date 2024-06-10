
def rearrange_string(s):
    n = len(s)
    if n % 2 == 1 or n > 10000:
        return "-1"
    
    # create a dictionary to store the frequency of each substring
    freq = {}
    for i in range(n - (n // 2) + 1):
        substring = s[i:i + n // 2]
        if substring not in freq:
            freq[substring] = 1
        else:
            freq[substring] += 1
    
    # if there is a substring that appears more than once, it is not possible to rearrange the string
    if any(freq.values()):
        return "-1"
    
    # rearrange the string
    result = ""
    for i in range(n // 2):
        for j in range(n // 2):
            if s[j] not in result:
                result += s[j]
                break
    
    return result

def main():
    s = input("Enter a string: ")
    print(rearrange_string(s))

if __name__ == '__main__':
    main()

