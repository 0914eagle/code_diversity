
def is_happy(message):
    message = message.lower()
    message_set = set(message)
    love_string = "iloveyou"
    love_set = set(love_string)
    if love_set.issubset(message_set):
        return "happy"
    else:
        return "sad"

def main():
    message = input("Enter the message: ")
    print(is_happy(message))

if __name__ == '__main__':
    main()

