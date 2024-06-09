
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

    def __str__(self):
        return self.string

def f1(program1, program2):
    # Initialize two empty strings
    str1 = LongLongString("")
    str2 = LongLongString("")

    # Iterate through the operations of both programs
    for op1, op2 in zip(program1, program2):
        # If the operations are the same, apply them to both strings
        if op1 == op2:
            apply_operation(str1, op1)
            apply_operation(str2, op2)
        # If the operations are different, return False
        else:
            return False

    # If all operations are the same, return True
    return True

def f2(program1, program2):
    # Initialize two empty strings
    str1 = LongLongString("")
    str2 = LongLongString("")

    # Iterate through the operations of both programs
    for op1, op2 in zip(program1, program2):
        # If the operations are the same, apply them to both strings
        if op1 == op2:
            apply_operation(str1, op1)
            apply_operation(str2, op2)
        # If the operations are different, return False
        else:
            return False

    # If all operations are the same, return True
    return True

def apply_operation(string, operation):
    # If the operation is a Del operation, delete the character at the specified position
    if operation[0] == 'D':
        del string[int(operation[2:])]
    # If the operation is an Ins operation, insert the specified character at the specified position
    elif operation[0] == 'I':
        string[int(operation[2:])] = operation[4]

if __name__ == '__main__':
    program1 = input().split()
    program2 = input().split()
    print(f1(program1, program2))
    print(f2(program1, program2))

