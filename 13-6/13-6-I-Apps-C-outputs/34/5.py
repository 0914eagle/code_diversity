
class LongLongString:
    def __init__(self, string):
        self.string = string

    def __len__(self):
        return len(self.string)

    def __getitem__(self, index):
        return self.string[index]

    def __setitem__(self, index, value):
        self.string = self.string[:index] + value + self.string[index+1:]

    def __delitem__(self, index):
        self.string = self.string[:index] + self.string[index+1:]

def f1(program1, program2):
    # Initialize two empty strings
    string1 = LongLongString("")
    string2 = LongLongString("")

    # Iterate through the operations of both programs
    for op1, op2 in zip(program1, program2):
        # If the operations are the same, apply them to both strings
        if op1 == op2:
            string1 = apply_operation(string1, op1)
            string2 = apply_operation(string2, op2)
        # If the operations are different, return False
        else:
            return False

    # If all operations are the same, return True
    return True

def f2(program1, program2):
    # Initialize two empty strings
    string1 = LongLongString("")
    string2 = LongLongString("")

    # Iterate through the operations of both programs
    for op1, op2 in zip(program1, program2):
        # If the operations are the same, apply them to both strings
        if op1 == op2:
            string1 = apply_operation(string1, op1)
            string2 = apply_operation(string2, op2)
        # If the operations are different, return False
        else:
            return False

    # If all operations are the same, return True
    return True

def apply_operation(string, operation):
    # If the operation is a Del operation, delete the character at the given position
    if operation[0] == "D":
        string.__delitem__(int(operation[1:]))
    # If the operation is an Ins operation, insert the given character at the given position
    elif operation[0] == "I":
        string.__setitem__(int(operation[1]), operation[3])

    return string

def main():
    # Read the two DNA editing programs from standard input
    program1 = input().split()
    program2 = input().split()

    # Check if the two programs are identical
    if f1(program1, program2):
        print("0")
    else:
        print("1")

if __name__ == '__main__':
    main()

