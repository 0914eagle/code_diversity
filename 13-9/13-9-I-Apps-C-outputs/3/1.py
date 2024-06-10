
class LongLongString:
    def __init__(self):
        self.string = ""

    def Ins(self, p, c):
        self.string = self.string[:p] + c + self.string[p:]

    def Del(self, p):
        self.string = self.string[:p] + self.string[p+1:]

def are_identical(program1, program2):
    string1 = LongLongString()
    string2 = LongLongString()
    for operation in program1:
        if operation[0] == "D":
            string1.Del(int(operation[1]))
        elif operation[0] == "I":
            string1.Ins(int(operation[1]), operation[2])
    for operation in program2:
        if operation[0] == "D":
            string2.Del(int(operation[1]))
        elif operation[0] == "I":
            string2.Ins(int(operation[1]), operation[2])
    return string1.string == string2.string

def main():
    program1 = []
    program2 = []
    while True:
        line = input()
        if line == "E":
            break
        operation = line.split()
        if operation[0] == "D":
            program1.append(operation)
        elif operation[0] == "I":
            program2.append(operation)
    print(are_identical(program1, program2))

if __name__ == '__main__':
    main()

