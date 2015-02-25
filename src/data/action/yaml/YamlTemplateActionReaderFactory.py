from src.data.action.yaml.YamlTemplateActionBuilder import YamlTemplateActionBuilder
from src.data.action.yaml.YamlTemplateActionReader import YamlTemplateActionReader

__author__ = 'DWI'

class YamlTemplateActionReaderFactory(object):



    def build(self):
        """
        Build a YAMLTemplateReader that is ready to use
        :return: a YAMLTemplateReader
        """
        return YamlTemplateActionReader(YamlTemplateActionBuilder())