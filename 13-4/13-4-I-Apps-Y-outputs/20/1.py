
import xml.etree.ElementTree as ET

def get_max_level(xml_string):
    root = ET.fromstring(xml_string)
    return get_level(root)

def get_level(element):
    level = 0
    for child in element:
        level = max(level, get_level(child) + 1)
    return level

if __name__ == '__main__':
    xml_string = sys.stdin.read()
    print(get_max_level(xml_string))

