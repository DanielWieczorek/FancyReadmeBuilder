"""
Module for Canvas
"""
__author__ = 'DWI'


class Canvas(object):
    """
    Class representing a rectangular drawing field consisting of characters.
    Its essentially a 2d character matrix
    """

    def __init__(self, background_string):
        if background_string:
            self.data_matrix = background_string.split("\n")
            for i in range(len(self.data_matrix)):
                self.data_matrix[i] = list(self.data_matrix[i])

    def draw(self, template_field):
        """
        Draws the given field onto this canvas
        :param template_field: the template field to draw
        """
        template_field.draw_onto(self)

    def get_string(self):
        """
        Returns the string representation of this canvas.
        A printable version of the 2d character matrix.
        :return: a string representation of this Canvas
        """
        result = ""
        for line in self.data_matrix:
            result += "".join(line)+'\n'

        return result[:-1]
