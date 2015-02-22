from src.data.InputFileType import InputFileType
from src.data.action.YamlTemplateActionReaderFactory import YamlTemplateActionReaderFactory

__author__ = 'DWI'

class TemplateActionReaderFactory(object):
    def __init__(self):
        self._mapping = {InputFileType.yaml: YamlTemplateActionReaderFactory()}

    def build_for_type(self, template_reader_type):
        """
        Build a Template of the given TemplateReaderType
        :param template_reader_type: type of the TemplateReader to build
        :return: the built template reader or None if there were no mapping
        """
        concrete_builder = self._mapping.get(template_reader_type)
        if concrete_builder:
            return concrete_builder.build()
        return None
