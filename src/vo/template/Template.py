"""
Module for Template
"""
__author__ = 'DWI'


class Template(object):
    """
    Class that represents the template and contains a list of fields.
    """

    def __init__(self, image, fields):
        """
        :param image: the background image e.g. ANSI art
        :param fields: the fields that can be drawn onto the background image
        """
        self._image = image
        self.field_list = list()
        self.field_list.append(fields)

    def __iter__(self):
        return iter(self.field_list)