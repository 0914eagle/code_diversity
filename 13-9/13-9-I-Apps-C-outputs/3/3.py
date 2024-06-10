
class LongLongString:
    def __init__(self, string):
        self.string = string

    def __len__(self):
        return len(self.string)

    def __getitem__(self, index):
        return self.string[index]

    def __setitem__(self, index, char):
        self.string = self.string[:index] + char + self.string[index + 1:]

    def __delitem__(self, index):
        self.string = self.string[:index] + self.string[index + 1:]

    def __str__(self):
        return self.string

def compare_programs(prog1, prog2):
    seq = LongLongString("")
    for op in prog1:
        if op[0] == "I":
            seq[int(op[1])] = op[2]
        elif op[0] == "D":
            del seq[int(op[1])]
    return seq == compare_programs(prog2, seq)

def parse_program(program):
    return [op.split() for op in program.split("\n") if op]

def main():
    prog1 = input("Enter the first program: ")
    prog2 = input("Enter the second program: ")
    prog1 = parse_program(prog1)
    prog2 = parse_program(prog2)
    print(compare_programs(prog1, prog2))

if __name__ == '__main__':
    main()

