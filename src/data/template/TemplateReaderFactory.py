"""
Module for TemplateReaderFactory
"""
from src.data.template.TemplateReaderType import TemplateReaderType
from src.data.template.yaml.YamlTemplateReaderFactory import YamlTemplateReaderFactory


__author__ = 'DWI'


class TemplateReaderFactory(object):
    """
    Factory base class for creating TemplateReader objects

    This class contains an internal mapping that has to be updated if a new TemplateReader type is added.
    """

    def __init__(self):
        self._mapping = {TemplateReaderType.yaml: YamlTemplateReaderFactory()}

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
