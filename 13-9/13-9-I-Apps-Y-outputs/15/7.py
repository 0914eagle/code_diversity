
def is_directory_number(number):
    return number // 1000000 == 555

def main():
    number = int(input())
    print(int(is_directory_number(number)))

if __name__ == '__main__':
    main()

