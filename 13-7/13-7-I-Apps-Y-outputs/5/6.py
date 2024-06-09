
def apaxian_name_extender(name, parent_name):
    if name.endswith('e'):
        return name + 'x' + parent_name
    elif name[-1] in 'aiou':
        return name[:-1] + 'ex' + parent_name
    elif name.endswith('ex'):
        return name + parent_name
    else:
        return name + 'ex' + parent_name

