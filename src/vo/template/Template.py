"""
Module for Template
"""
from src.vo.render.Canvas import Canvas

__author__ = 'DWI'


class Template(object):
    """
    Class that represents the template and contains a list of fields.
    """

    def __init__(self, image, fields, name):
        """
        :param image: the background image e.g. ANSI art
        :param fields: the fields that can be drawn onto the background image
        """
        self._image = Canvas(image)
        self.field_list = list()
        self.name = name
        if isinstance(fields,list):
            self.field_list.extend(fields)
        else:
            self.field_list.append(fields)

    def __iter__(self):
        return iter(self.field_list)


    def render(self):
        """
        Draws the fields of this template on its background image and
        returns the resulting string
        :return: the string of the background and the field drawn onto it
        """
        for field in self.field_list:
            self._image.draw(field)

        return self._image.get_string()