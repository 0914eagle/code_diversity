
def check_happiness(message):
    if "iloveyou" in message:
        return "happy"
    else:
        return "sad"

def main():
    message = input("Enter the message: ")
    print(check_happiness(message))

if __name__ == '__main__':
    main()

