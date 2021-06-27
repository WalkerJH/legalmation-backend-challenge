import complaint_parser

input_folder = '../input'

def test_parse_plaintiffs_a():
    assert complaint_parser.get_plaintiffs_from_xml(input_folder + '/A.xml') == ['ANGELO ANGELES, an individial']

def test_parse_plaintiffs_b():
    assert complaint_parser.get_plaintiffs_from_xml(input_folder + '/B.xml') == ['KUSUMA AMBELGAR']

def test_parse_plaintiffs_c():
    assert complaint_parser.get_plaintiffs_from_xml(input_folder + '/C.xml') == ['KUSUMA AMBELGAR']

def test_parse_defendants_a():
    assert complaint_parser.get_defendants_from_xml(input_folder + '/A.xml') == ['ANGELO ANGELES, an individial']

def test_parse_defendants_b():
    assert complaint_parser.get_defendants_from_xml(input_folder + '/B.xml') == ['KUSUMA AMBELGAR']

def test_parse_defendants_c():
    assert complaint_parser.get_defendants_from_xml(input_folder + '/C.xml') == ['KUSUMA AMBELGAR']