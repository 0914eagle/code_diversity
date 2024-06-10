
def check_message(message):
    return "happy" if "iloveyou" in message else "sad"

def main():
    message = input("Enter the message received by Bhopu: ")
    print(check_message(message))

if __name__ == '__main__':
    main()

