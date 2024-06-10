
def shift_message(direction, message):
    if direction == "L":
        return "".join([chr(ord(c) - 1) for c in message])
    elif direction == "R":
        return "".join([chr(ord(c) + 1) for c in message])
    else:
        raise ValueError("Invalid direction")

def decode_message(message):
    # Split the message into rows of length 10
    rows = [message[i:i+10] for i in range(0, len(message), 10)]
    # Initialize the decoded message as an empty string
    decoded_message = ""
    # Loop through the rows of the message
    for row in rows:
        # Get the direction of shifting for this row
        direction = row[0]
        # Get the message for this row
        row_message = row[1:]
        # Decode the message for this row
        decoded_row = shift_message(direction, row_message)
        # Add the decoded row to the decoded message
        decoded_message += decoded_row
    return decoded_message

def main():
    direction = input("Enter the direction of shifting (L or R): ")
    message = input("Enter the message: ")
    decoded_message = decode_message(message)
    print(decoded_message)

if __name__ == '__main__':
    main()

