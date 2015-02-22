from src.data.action.TemplateActionBuilder import TemplateActionBuilder

__author__ = 'DWI'



class YamlTemplateActionBuilder(TemplateActionBuilder):


    def __init__(self):
        super(YamlTemplateActionBuilder, self).__init__()

    def build(self, data):
        field_name = next(iter(data))
        type = data.get(field_name).get("type")
        value = data.get(field_name).get("value")

        action = self._get_action_instance(type)
        action.field_name = field_name
        action.value = value
        return action