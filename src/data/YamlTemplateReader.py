import yaml
from src.data.TemplateReader import TemplateReader
from src.vo.template.Template import Template

__author__ = 'DWI'


class YamlTemplateReader(TemplateReader):

    def __init__(self, template_field_builder):
        self.field_builder = template_field_builder

    def _load_data(self, file):
        data = yaml.load(file)
        return data.get(next(iter(data)))

    def _build_template(self, template_data):
        field_list = list()
        for field_name in template_data.keys():
            field_list.append(self.field_builder.build({field_name:template_data.get(field_name)}))

        return Template(None, field_list)