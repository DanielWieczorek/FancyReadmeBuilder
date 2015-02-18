import ast
from src.data.TemplateFieldBuilder import TemplateFieldBuilder
from src.vo.template.RectangularTemplateField import RectangularTemplateField

__author__ = 'DWI'

class YamlTemplateFieldBuilder(TemplateFieldBuilder):

    def __init__(self):
        super(YamlTemplateFieldBuilder, self).__init__()


    def build(self,data):
        field_name = next(iter(data))
        field_data = data.get(field_name)
        field_type = field_data.get("type")

        result_field = self._get_field_instance(field_type)
        result_field.name = field_name
        result_field.start_point = ast.literal_eval(field_data.get("start_coord"))
        result_field.end_point = ast.literal_eval(field_data.get("start_coord"))

        return result_field