
def get_min_replacements(ai_name, phone_name):
    replacements = 0
    for i in range(len(ai_name)):
        if ai_name[i:i+len(phone_name)] == phone_name:
            replacements += 1
    return replacements

def main():
    ai_name = input("Enter the name of the AI: ")
    phone_name = input("Enter the name of the phone: ")
    print(get_min_replacements(ai_name, phone_name))

if __name__ == '__main__':
    main()

