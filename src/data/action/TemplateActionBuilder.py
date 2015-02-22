from copy import copy

from src.model.action.TemplateFieldUpdate import TemplateFieldUpdate


__author__ = 'DWI'


class TemplateActionBuilder(object):

    def __init__(self):
        self._action_mapping = {"update": TemplateFieldUpdate(None, None)}

    def build(self, data):
        """
        Builds the TemplateField from the given data.
        :param data: data that contains all information for building the TemplateField
        :return: The template field or None if the specified type was invalid
        """
        pass

    def _get_action_instance(self, field_type):
        original_action = self._action_mapping.get(field_type)
        if original_action:
            return copy(original_action)
        return None