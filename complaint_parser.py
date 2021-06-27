import xml.etree.ElementTree as ET

def get_defendants_from_xml(fileName):
    tree = ET.parse(fileName)
    root = tree.getroot()

    return ['NOT IMPLEMENTED']


def get_plaintiffs_from_xml(fileName):
    tree = ET.parse(fileName)
    root = tree.getroot()

    return ['NOT IMPLEMENTED']
