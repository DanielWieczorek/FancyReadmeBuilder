"""
Module for TemplateFieldUpdate
"""
from src.vo.action.TemplateFieldAction import TemplateFieldAction

__author__ = 'DWI'


class TemplateFieldUpdate(TemplateFieldAction):
    """
    Class representing an action that changes its value.
    """

    def __init__(self, field_name, value):
        super(TemplateFieldUpdate, self).__init__(field_name, value)

    def _apply_to_field(self, template, field):
        """
        Sets the fields value to the value within this action.
        Only the first n characters of this actions value are used as fields value
        where field n is the number of characters the field can hold.
        :param template: not used by this class
        :param field: the field to be altered
        """
        field.value = self.value[:field.get_size()]
