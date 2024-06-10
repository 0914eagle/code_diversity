
def check_hiss(word):
    if 's' * 2 in word:
        return 'hiss'
    else:
        return 'no hiss'

def main():
    word = input()
    print(check_hiss(word))

if __name__ == '__main__':
    main()

