from src.vo.template.RectangularTemplateField import RectangularTemplateField
from copy import copy
__author__ = 'DWI'


class TemplateFieldBuilder(object):

    def __init__(self):
        self._field_mapping = {"rect": RectangularTemplateField(None,(0,0),(0,0))}

    def build(self, data):
        pass


    def _get_field_instance(self, field_type):
        original_field = self._field_mapping.get(field_type)
        if original_field:
            return copy(original_field)
        return None