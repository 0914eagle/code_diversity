
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
    seq1 = LongLongString("")
    seq2 = LongLongString("")
    for op in program1:
        if op[0] == "D":
            seq1.__delitem__(int(op[1]))
        elif op[0] == "I":
            seq1.__setitem__(int(op[1]), op[2])
    for op in program2:
        if op[0] == "D":
            seq2.__delitem__(int(op[1]))
        elif op[0] == "I":
            seq2.__setitem__(int(op[1]), op[2])
    return seq1 == seq2

def f2(program1, program2):
    seq1 = LongLongString("")
    seq2 = LongLongString("")
    for op in program1:
        if op[0] == "D":
            seq1.__delitem__(int(op[1]))
        elif op[0] == "I":
            seq1.__setitem__(int(op[1]), op[2])
    for op in program2:
        if op[0] == "D":
            seq2.__delitem__(int(op[1]))
        elif op[0] == "I":
            seq2.__setitem__(int(op[1]), op[2])
    return seq1 == seq2

if __name__ == '__main__':
    program1 = []
    program2 = []
    while True:
        line = input()
        if line == "E":
            break
        op = line.split()
        if op[0] == "D":
            program1.append(("D", int(op[1])))
            program2.append(("D", int(op[1])))
        elif op[0] == "I":
            program1.append(("I", int(op[1]), op[2]))
            program2.append(("I", int(op[1]), op[2]))
    print(f1(program1, program2))
    print(f2(program1, program2))

