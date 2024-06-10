
def is_happy(message):
    return "iloveyou" in message

def main():
    message = input("Enter the message: ")
    if is_happy(message):
        print("happy")
    else:
        print("sad")

if __name__ == '__main__':
    main()

