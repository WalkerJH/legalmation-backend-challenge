import xml.etree.ElementTree as ET

def getDefendantsFromXml(fileName):
    tree = ET.parse(fileName)
    root = tree.getroot()

    return ['NOT IMPLEMENTED']


def getPlaintiffsFromXml(fileName):
    tree = ET.parse(fileName)
    root = tree.getroot()

    return ['NOT IMPLEMENTED']
