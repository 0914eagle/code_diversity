
def is_beautiful(w):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    count = [0] * 26
    for c in w:
        if c in alphabet:
            count[ord(c) - ord("a")] += 1
    for c in count:
        if c % 2 != 0:
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

