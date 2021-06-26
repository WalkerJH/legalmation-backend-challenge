import complaintParser

input_folder = '../input'

def test_parse_plaintiffs_a():
    assert complaintParser.getPlaintiffsFromXml(input_folder + '/A.xml') == ['ANGELO ANGELES, an individial']

def test_parse_plaintiffs_b():
    assert complaintParser.getPlaintiffsFromXml(input_folder + '/B.xml') == ['KUSUMA AMBELGAR']

def test_parse_plaintiffs_c():
    assert complaintParser.getPlaintiffsFromXml(input_folder + '/C.xml') == ['KUSUMA AMBELGAR']