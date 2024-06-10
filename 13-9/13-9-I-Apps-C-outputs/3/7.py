
class LongLongString:
    def __init__(self, string):
        self.string = string

    def insert(self, p, c):
        self.string = self.string[:p] + c + self.string[p:]

    def delete(self, p):
        self.string = self.string[:p] + self.string[p+1:]

def is_identical(program1, program2):
    string1 = LongLongString("")
    string2 = LongLongString("")

    for op in program1:
        if op[0] == "I":
            string1.insert(int(op[1]), op[2])
        elif op[0] == "D":
            string1.delete(int(op[1]))

    for op in program2:
        if op[0] == "I":
            string2.insert(int(op[1]), op[2])
        elif op[0] == "D":
            string2.delete(int(op[1]))

    return string1.string == string2.string

def main():
    program1 = []
    program2 = []

    while True:
        line = input()
        if line == "E":
            break
        else:
            op = line.split()
            if op[0] == "I":
                program1.append(["I", int(op[1]), op[2]])
            elif op[0] == "D":
                program1.append(["D", int(op[1])])

    while True:
        line = input()
        if line == "E":
            break
        else:
            op = line.split()
            if op[0] == "I":
                program2.append(["I", int(op[1]), op[2]])
            elif op[0] == "D":
                program2.append(["D", int(op[1])])

    if is_identical(program1, program2):
        print("0")
    else:
        print("1")

if __name__ == '__main__':
    main()

