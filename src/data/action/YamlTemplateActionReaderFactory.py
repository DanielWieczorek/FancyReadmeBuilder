from src.data.action.YamlTemplateActionBuilder import YamlTemplateActionBuilder
from src.data.action.YamlTemplateActionReader import YamlTemplateActionReader

__author__ = 'DWI'

class YamlTemplateActionReaderFactory(object):



    def build(self):
        """
        Build a YAMLTemplateReader that is ready to use
        :return: a YAMLTemplateReader
        """
        return YamlTemplateActionReader(YamlTemplateActionBuilder())