
def is_beautiful(w):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    count = [0] * 26
    for c in w:
        index = ord(c) - ord("a")
        count[index] += 1
    for i in range(26):
        if count[i] % 2 == 1:
            return False
    return True

def main():
    w = input()
    if is_beautiful(w):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

