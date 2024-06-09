
class LongLongString:
    def __init__(self, string):
        self.string = string

    def __len__(self):
        return len(self.string)

    def __getitem__(self, key):
        return self.string[key]

    def __setitem__(self, key, value):
        self.string = self.string[:key] + value + self.string[key+1:]

    def __delitem__(self, key):
        self.string = self.string[:key] + self.string[key+1:]

    def __str__(self):
        return self.string

def parse_operation(operation):
    op, pos = operation.split()
    pos = int(pos)
    if op == "D":
        return ("D", pos)
    elif op == "I":
        return ("I", pos)
    else:
        raise ValueError("Invalid operation")

def apply_operation(string, operation):
    op, pos = operation
    if op == "D":
        del string[pos]
    elif op == "I":
        string[pos] = "X"
    else:
        raise ValueError("Invalid operation")
    return string

def compare_programs(program1, program2):
    string1 = LongLongString("")
    string2 = LongLongString("")
    for operation in program1:
        apply_operation(string1, operation)
    for operation in program2:
        apply_operation(string2, operation)
    return string1 == string2

def main():
    program1 = []
    program2 = []
    while True:
        operation = input()
        if operation == "E":
            break
        program1.append(parse_operation(operation))
    while True:
        operation = input()
        if operation == "E":
            break
        program2.append(parse_operation(operation))
    if compare_programs(program1, program2):
        print("0")
    else:
        print("1")

if __name__ == '__main__':
    main()

