"""
Module for YamlTemplateReader
"""
import yaml

from src.data.TemplateReader import TemplateReader
from src.vo.template.Template import Template


__author__ = 'DWI'


class YamlTemplateReader(TemplateReader):
    """
    Class that for reading a whole template from A YAML document
    The document is structured as follows:
    test:
     foo:
      start_coord: (1,2)
      end_coord: (2,2)
      type: rect

    'test0' is the name of the template and 'foo' is the name of the first field
    Ony the first template entry is read.
    """

    def __init__(self, template_field_builder):
        super(YamlTemplateReader, self).__init__(template_field_builder)

    def _load_data(self, file):
        """
        returns the first top level entry of this yaml document
        :param file: YAML file that contains the template
        :return: a dictionary representing the document.
        """
        return yaml.load(file)

    def _build_template(self, template_data):
        """
        Builds the actual template from the input yaml data
        :param template_data: the data for the template
        :return: a new template object containing all the data for
        """
        template_name = next(iter(template_data))
        template_content = template_data.get(template_name)
        field_list = list()
        for field_name in template_content.keys():
            field_list.append(self.field_builder.build({field_name:template_content.get(field_name)}))

        return Template(None, field_list, template_name)