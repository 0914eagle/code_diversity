
class LongLongString:
    def __init__(self, string):
        self.string = string

    def insert(self, pos, char):
        self.string = self.string[:pos] + char + self.string[pos:]

    def delete(self, pos):
        self.string = self.string[:pos] + self.string[pos+1:]

def is_identical(program1, program2):
    # Create two LongLongString objects for each program
    str1 = LongLongString("")
    str2 = LongLongString("")

    # Apply the operations in each program to their corresponding string
    for op in program1:
        if op[0] == "D":
            str1.delete(int(op[1]))
        elif op[0] == "I":
            str1.insert(int(op[1]), op[2])

    for op in program2:
        if op[0] == "D":
            str2.delete(int(op[1]))
        elif op[0] == "I":
            str2.insert(int(op[1]), op[2])

    # Compare the two strings and return whether they are identical
    return str1.string == str2.string

def get_program(input_str):
    program = []
    for line in input_str.splitlines():
        if line.startswith("D"):
            program.append(["D", line[2:].strip()])
        elif line.startswith("I"):
            program.append(["I", line[2:].strip()])
    return program

def main():
    program1 = get_program(input())
    program2 = get_program(input())
    if is_identical(program1, program2):
        print("0")
    else:
        print("1")

if __name__ == '__main__':
    main()

