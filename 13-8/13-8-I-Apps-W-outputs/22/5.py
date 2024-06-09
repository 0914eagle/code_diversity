
def is_possible(c_charges, t_charges):
    if len(c_charges) != len(t_charges):
        return "No"
    
    for i in range(1, len(c_charges) - 1):
        if c_charges[i] != t_charges[i]:
            if c_charges[i-1] + c_charges[i+1] - c_charges[i] != t_charges[i]:
                return "No"
            else:
                c_charges[i] = t_charges[i]
    
    return "Yes"

