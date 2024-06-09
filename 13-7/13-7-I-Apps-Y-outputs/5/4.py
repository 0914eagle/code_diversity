
def extended_name(name, parent):
    if name.endswith('e'):
        return name + 'x' + parent
    elif name[-1] in 'aiou':
        return name[:-1] + 'ex' + parent
    else:
        return name + 'ex' + parent

