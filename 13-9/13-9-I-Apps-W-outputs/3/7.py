
def check_message(message):
    return "happy" if set("iloveyou") <= set(message) else "sad"

def main():
    message = input("Enter the message: ")
    print(check_message(message))

if __name__ == '__main__':
    main()

