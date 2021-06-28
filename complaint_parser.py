import xml.etree.ElementTree as ET

def get_defendants_from_xml(xml_text):
    root = ET.fromstring(xml_text)

    defendants_found = False
    defendants_str = ''
    for line in root.findall('page'):
        print(line.tag)
        # if 'vs.' in line.text:
        #     defendants_found = True
        # if 'Defendants.' in line.text:
        #     return defendants_str

        # if defendants_found:
        #     defendants_str += line.text
        return "hi"


def get_plaintiffs_from_xml(xml_text):
    root = ET.fromstring(xml_text)

    return 'NOT IMPLEMENTED'