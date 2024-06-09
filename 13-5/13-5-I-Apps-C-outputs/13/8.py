
def get_phone_numbers(s):
    phone_numbers = []
    for i in range(len(s) - 10):
        if s[i] == "8" and s[i + 1:i + 11].isdigit():
            phone_numbers.append(s[i:i + 11])
    return phone_numbers

def get_max_phone_numbers(s):
    phone_numbers = get_phone_numbers(s)
    return len(phone_numbers)

def main():
    n = int(input())
    s = input()
    print(get_max_phone_numbers(s))

if __name__ == '__main__':
    main()

