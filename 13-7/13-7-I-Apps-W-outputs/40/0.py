
def is_telephone_number(s):
    return len(s) == 11 and s[0] == '8' and s.isdigit()

def has_winning_strategy(s):
    if len(s) == 1:
        return is_telephone_number(s)
    
    if len(s) % 2 == 0:
        return False
    
    for i in range(len(s)):
        if is_telephone_number(s[:i] + s[i+1:]):
            return True
    
    return False

def main():
    n = int(input())
    s = input()
    print("YES") if has_winning_strategy(s) else print("NO")

if __name__ == '__main__':
    main()

