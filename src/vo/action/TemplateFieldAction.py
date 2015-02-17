"""
Module for TemplateFieldAction
"""
from src.vo.action.TemplateAction import TemplateAction

__author__ = 'DWI'


class TemplateFieldAction(TemplateAction):
    """
    Class representing an action onto a field, e.g. updating the value
    """

    def __init__(self, field_name, value=None):
        self.field_name = field_name
        self.value = value

    def get_field(self, template):
        """
        Retrieves the first field this action is applied to
        :param template: the template within which the field is searches
        :return: the field found or none
        """
        for field in template:
            if self.field_name == field.name:
                return field
        return None

    def apply_to(self, template):
        """
        Applies this update to Template. In the end this update will be applied
        to a field within this Template
        :param template: the template to apply the Action to
        """
        field = self.get_field(template)
        self._apply_to_field(template, field)

    def _apply_to_field(self, template, field):
        pass