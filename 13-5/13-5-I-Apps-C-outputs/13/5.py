
def f1(n, s):
    # find all possible phone numbers in the string
    phone_numbers = []
    for i in range(len(s)-10):
        if s[i] == '8' and s[i+1:i+11].isdigit():
            phone_numbers.append(s[i:i+11])
    
    # remove duplicates
    phone_numbers = list(set(phone_numbers))
    
    return len(phone_numbers)

def f2(n, s):
    # find all possible phone numbers in the string
    phone_numbers = []
    for i in range(len(s)-10):
        if s[i] == '8' and s[i+1:i+11].isdigit():
            phone_numbers.append(s[i:i+11])
    
    # remove duplicates
    phone_numbers = list(set(phone_numbers))
    
    # print the maximum number of phone numbers that can be made
    print(len(phone_numbers))

if __name__ == '__main__':
    n = int(input())
    s = input()
    f2(n, s)

