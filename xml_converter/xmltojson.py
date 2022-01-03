from collections import defaultdict
from xml.etree import ElementTree


class XMLToJson:

    def __init__(self, xmlfile):
        tree = ElementTree.parse(xmlfile)
        root = tree.getroot()
        self.result = self._xml_to_json_recursive(root)

    def _xml_to_json_recursive(self, elem):
        result = {elem.tag: [] if elem.attrib else ''}
        child = list(elem)
        if child and elem.tag:
            temp_dict = defaultdict(list)
            for data_dict in map(self._xml_to_json_recursive, child):
                for k, v in data_dict.items():
                    temp_dict[elem.tag].append({k:v})

            result = {k: v for k, v in temp_dict.items()}

        if elem.text and elem.text.strip():
            result[elem.tag] = elem.text.strip()

        return result        
