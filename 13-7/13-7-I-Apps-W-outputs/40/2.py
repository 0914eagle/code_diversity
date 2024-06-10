
def check_winning_strategy(s):
    n = len(s)
    if n == 11:
        return True
    elif n == 1:
        return False
    else:
        for i in range(n):
            if s[i] == '8':
                if check_winning_strategy(s[:i] + s[i+1:]) == True:
                    return True
        return False

def main():
    n = int(input())
    s = input()
    if check_winning_strategy(s) == True:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

