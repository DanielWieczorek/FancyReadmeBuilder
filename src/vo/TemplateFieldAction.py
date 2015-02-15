from src.vo.TemplateAction import TemplateAction

__author__ = 'DWI'


class TemplateFieldAction(TemplateAction):
    def __init__(self, field_name, value=None):
        self.field_name = field_name
        self.value = value

    def get_field(self, template):
        for field in template:
            if self.field_name == field.name:
                return field

    def apply_to(self, template):
        field = self.get_field(template)
        self._apply_to_field(template, field)

    def _apply_to_field(self, template, field):
        pass