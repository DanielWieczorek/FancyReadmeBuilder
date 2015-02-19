import yaml
from src.vo.template.Template import Template

__author__ = 'DWI'


class TemplateReader(object):

    def __init__(self, templateFieldBuilder):
        self.field_builder = templateFieldBuilder


    def read(self, file_name):
        data = None
        with open(file_name, 'r') as file:
            data = self._load_data(file)
        return self._build_template(data)

    def _load_data(self, file):
        pass

    def _build_template(self, template_data):
        pass