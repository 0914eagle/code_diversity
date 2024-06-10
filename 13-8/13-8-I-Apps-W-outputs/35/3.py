
def get_min_changes(ai_name, phone_name):
    ai_name = ai_name.lower()
    phone_name = phone_name.lower()
    changes = 0
    for i in range(len(ai_name)):
        if ai_name[i:i+len(phone_name)] == phone_name:
            changes += 1
    return changes

def get_new_ai_name(ai_name, phone_name, changes):
    new_ai_name = ""
    for i in range(len(ai_name)):
        if ai_name[i:i+len(phone_name)] == phone_name:
            new_ai_name += "#"
        else:
            new_ai_name += ai_name[i]
    return new_ai_name

if __name__ == '__main__':
    ai_name = input("Enter the name of the AI: ")
    phone_name = input("Enter the name of the phone: ")
    changes = get_min_changes(ai_name, phone_name)
    new_ai_name = get_new_ai_name(ai_name, phone_name, changes)
    print(f"The minimum number of characters to replace is {changes}")
    print(f"The new name of the AI is {new_ai_name}")

