
def is_happy(message):
    return "iloveyou" in message

def is_sad(message):
    return "iloveyou" not in message

def main():
    message = input("Enter the message: ")
    if is_happy(message):
        print("Happy")
    else:
        print("Sad")

if __name__ == '__main__':
    main()

