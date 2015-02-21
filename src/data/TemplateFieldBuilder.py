"""
Module for TemplateFieldBuilder
"""
from copy import copy

from src.model.template.RectangularTemplateField import RectangularTemplateField

__author__ = 'DWI'


class TemplateFieldBuilder(object):
    """
    Abstract base class for classes building templates from files
    """

    def __init__(self):
        self._field_mapping = {"rect": RectangularTemplateField(None,(0,0),(0,0))}

    def build(self, data):
        """
        Builds the TemplateField from the given data.
        :param data: data that contains all information for building the TemplateField
        :return: The template field or None if the specified type was invalid
        """
        pass


    def _get_field_instance(self, field_type):
        original_field = self._field_mapping.get(field_type)
        if original_field:
            return copy(original_field)
        return None