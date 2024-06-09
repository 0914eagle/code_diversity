
def simon_says(commands):
    output = []
    for command in commands:
        if command.startswith("Simon says"):
            output.append(command[11:])
    return output

