
def shift_message(direction, message):
    if direction == "L":
        return "".join(chr((ord(c) - 1) % 26 + ord('a')) for c in message)
    else:
        return "".join(chr((ord(c) + 1) % 26 + ord('a')) for c in message)

def decrypt_message(message):
    message = message.upper()
    rows = [
        "qwertyuiop",
        "asdfghjkl;",
        "zxcvbnm,./"
    ]
    result = []
    for c in message:
        for row in rows:
            if c in row:
                result.append(row[row.index(c) - 1])
                break
    return "".join(result)

def main():
    direction = input("Enter the direction of shift (L/R): ")
    message = input("Enter the message: ")
    shifted_message = shift_message(direction, message)
    decrypted_message = decrypt_message(shifted_message)
    print(f"The original message is: {decrypted_message}")

if __name__ == '__main__':
    main()

