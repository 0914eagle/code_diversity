
import xml.etree.ElementTree as ET

def get_max_depth(xml_string):
    root = ET.fromstring(xml_string)
    return get_depth(root)

def get_depth(element):
    if element.findall("./*"):
        return 1 + max(get_depth(child) for child in element)
    return 1

if __name__ == '__main__':
    xml_string = sys.stdin.read()
    print(get_max_depth(xml_string))

