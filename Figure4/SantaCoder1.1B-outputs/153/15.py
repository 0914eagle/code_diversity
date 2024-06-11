def Strongest_Extension(class_name, extensions):
    
    # Write your code here.
    return class_name + '.' + max(extensions, key=len)

# Example:
# Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'

# Strongest_Extension('my_class', ['AA', 'Be', 'CC', 'DD']) == 'my_class.DD'

# Strong