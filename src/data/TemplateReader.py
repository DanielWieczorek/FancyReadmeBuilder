import yaml
from src.vo.template.Template import Template

__author__ = 'DWI'


class TemplateReader(object):

    def __init__(self, templateFieldBuilder):
        self.field_builder = templateFieldBuilder


    def read(self, file_name):
        data = None
        with open(file_name, 'r') as yaml_file:
            data = yaml.load(yaml_file)
        return self._build_template(data.get(next(iter(data))))


    def _build_template(self, template_data):
        field_list = list()
        for field_name in template_data.keys():
            field_list.append(self.field_builder.build({field_name:template_data.get(field_name)}))

        return Template(None, field_list)