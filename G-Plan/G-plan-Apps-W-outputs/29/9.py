
def soroban_representation(n):
    def digit_representation(digit):
        if digit == 0:
            return "O-|-OOOO"
        elif digit == 1:
            return "O-|OOOO-"
        elif digit == 2:
            return "O-|OOO-O"
        elif digit == 3:
            return "O-|OO-OO"
        elif digit == 4:
            return "O-|O-OOO"
        elif digit == 5:
            return "O-|O-OO-"
        elif digit == 6:
            return "O-|O--OO"
        elif digit == 7:
            return "O-|-OOO-"
        elif digit == 8:
            return "O-|-OO-O"
        elif digit == 9:
            return "O-|-O-OO"

    digits = [int(d) for d in str(n)]
    for i in range(len(digits) - 1, -1, -1):
        print(digit_representation(digits[i]))

if __name__ == "__main__":
    n = int(input())
    soroban_representation(n)
