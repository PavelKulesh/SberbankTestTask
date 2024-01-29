import xml.etree.ElementTree as ET

from src.abstract.service import AbstractService
from src.formatters.date_formatter import DateFormatter


class XMLService(AbstractService):
    @classmethod
    def parse(cls, tree: str) -> dict:
        tree_dict = cls.__convert_xml_to_dict(tree)
        DateFormatter.normalize(tree_dict)
        return tree_dict

    @classmethod
    def __convert_xml_to_dict(cls, xml_data: str) -> dict:
        root = ET.fromstring(xml_data)
        result_dict = {}
        for element in root:
            if len(element) == 0:
                result_dict[element.tag] = element.text
            else:
                result_dict[element.tag] = {}
                for sub_element in element:
                    result_dict[element.tag][sub_element.tag] = sub_element.text
        return result_dict
