
class LongLongString:
    def __init__(self, string):
        self.string = string

    def insert(self, pos, char):
        self.string = self.string[:pos] + char + self.string[pos:]

    def delete(self, pos):
        self.string = self.string[:pos] + self.string[pos+1:]

    def __eq__(self, other):
        return self.string == other.string

def parse_program(program):
    operations = []
    for line in program.splitlines():
        if line.startswith("D"):
            pos = int(line.split()[1])
            operations.append(("D", pos))
        elif line.startswith("I"):
            pos, char = line.split()[1:]
            operations.append(("I", int(pos), char))
    return operations

def apply_operations(string, operations):
    llstring = LongLongString(string)
    for op, *args in operations:
        if op == "D":
            llstring.delete(args[0])
        elif op == "I":
            llstring.insert(args[0], args[1])
    return llstring

def compare_programs(program1, program2):
    operations1 = parse_program(program1)
    operations2 = parse_program(program2)
    string = "*" * 1000000000
    llstring1 = apply_operations(string, operations1)
    llstring2 = apply_operations(string, operations2)
    return llstring1 == llstring2

if __name__ == '__main__':
    program1 = 
    program2 = 
    print(compare_programs(program1, program2))


