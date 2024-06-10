
class LongLongString:
    def __init__(self):
        self.string = ''

    def insert(self, position, character):
        self.string = self.string[:position] + character + self.string[position:]

    def delete(self, position):
        self.string = self.string[:position] + self.string[position + 1:]

def compare_programs(program1, program2):
    seq = LongLongString()
    for operation in program1:
        if operation[0] == 'D':
            seq.delete(operation[1])
        elif operation[0] == 'I':
            seq.insert(operation[1], operation[2])
    return seq.string == compare_programs(program2, seq)

def main():
    program1 = []
    program2 = []
    for _ in range(2):
        while True:
            line = input()
            if line == 'E':
                break
            if line[0] == 'D':
                program1.append(('D', int(line[2:])))
            elif line[0] == 'I':
                program1.append(('I', int(line[2:line.find(' ')]), line[line.find(' ') + 1]))
        while True:
            line = input()
            if line == 'E':
                break
            if line[0] == 'D':
                program2.append(('D', int(line[2:])))
            elif line[0] == 'I':
                program2.append(('I', int(line[2:line.find(' ')]), line[line.find(' ') + 1]))
    print(compare_programs(program1, program2))

if __name__ == '__main__':
    main()

