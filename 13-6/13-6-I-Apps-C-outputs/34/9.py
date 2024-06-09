
class DNA:
    def __init__(self, dna_string):
        self.dna_string = dna_string

    def __eq__(self, other):
        return self.dna_string == other.dna_string

    def __ne__(self, other):
        return self.dna_string != other.dna_string

    def __repr__(self):
        return self.dna_string

    def __str__(self):
        return self.dna_string

    def apply_operation(self, operation):
        if operation[0] == "D":
            position = int(operation[1])
            self.dna_string = self.dna_string[:position-1] + self.dna_string[position:]
        elif operation[0] == "I":
            position = int(operation[1])
            character = operation[2]
            self.dna_string = self.dna_string[:position-1] + character + self.dna_string[position-1:]
        else:
            raise ValueError("Invalid operation")

def compare_dna_programs(dna_program_1, dna_program_2):
    dna_1 = DNA("")
    dna_2 = DNA("")
    for operation in dna_program_1:
        dna_1.apply_operation(operation)
    for operation in dna_program_2:
        dna_2.apply_operation(operation)
    if dna_1 == dna_2:
        return "0"
    else:
        return "1"

def main():
    dna_program_1 = input().split()
    dna_program_2 = input().split()
    print(compare_dna_programs(dna_program_1, dna_program_2))

if __name__ == '__main__':
    main()

