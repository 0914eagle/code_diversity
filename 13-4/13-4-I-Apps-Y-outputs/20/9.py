
import xml.etree.ElementTree as ET

def get_max_depth(xml_string):
    root = ET.fromstring(xml_string)
    return get_depth(root)

def get_depth(element):
    if element:
        return 1 + max(get_depth(child) for child in element)
    else:
        return 0

if __name__ == '__main__':
    num_lines = int(input())
    xml_string = ''
    for _ in range(num_lines):
        xml_string += input()
    print(get_max_depth(xml_string))

