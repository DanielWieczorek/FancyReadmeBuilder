from src.vo.TemplateFieldAction import TemplateFieldAction

__author__ = 'DWI'


class TemplateFieldUpdate(TemplateFieldAction):

    def __init__(self, field_name, value):
        super(TemplateFieldUpdate, self).__init__(field_name, value)

    def _apply_to_field(self, template, field):
        field.value = self.value[:field.get_size()]


