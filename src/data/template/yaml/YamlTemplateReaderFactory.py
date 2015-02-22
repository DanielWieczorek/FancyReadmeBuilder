"""
Module for YamlTemplateReaderFactory
"""
from src.data.template.yaml.YamlTemplateFieldBuilder import YamlTemplateFieldBuilder
from src.data.template.yaml.YamlTemplateReader import YamlTemplateReader

__author__ = 'DWI'


class YamlTemplateReaderFactory(object):
    """
    Class for building TemplateReaders that read YAML files
    """
    
    def __init__(self):
        super(YamlTemplateReaderFactory, self).__init__()

    def build(self):
        """
        Build a YAMLTemplateReader that is ready to use
        :return: a YAMLTemplateReader
        """
        return YamlTemplateReader(YamlTemplateFieldBuilder())