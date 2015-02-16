"""
Module for TemplateField
"""

__author__ = 'DWI'


class TemplateField(object):
    """
    Abstract base class for all fields within a template.
    A field is has an area that it covers defined by its upper left and lower right corner.
    It also has a value (text) and can be drawn onto a canvas object.

    The shape and other specialities are defined in the sub classes of this class
    """
    X = 0
    Y = 1

    def __init__(self, name, start_point, end_point):
        """
        :param name: name of this field
        :param start_point: coordinates of the upper left corner of this field.
        :param end_point: coordinates of the bottom right corner of the field
        """
        self.name = name
        self.value = None
        self.start_point = start_point
        self.end_point = end_point

    def get_size(self):
        """
        Returns the number of characters that fit into this field.
        The actual calculation depends on the implementation in the concrete subclass
        and e.g. the shape of the field.
        :rtype : integer
        :return: the size of this field
        """
        pass

    def __iter__(self):
        return self

    def draw_onto(self, canvas):
        """
        "Draws" this TemplateField onto the given Canvas.
        The canvas is a matrix of characters. Drawing means that the characters in the area defined by this field
        are replaced with the characters from the value of the field.

        :param canvas: canvas to "draw" on
        """
        canvas_data = canvas.data_matrix
        current_index = 0
        if self.value is not None:
            for character in self.value:
                coordinates = self._get_coordinates(current_index)
                canvas_data[coordinates[self.Y]][coordinates[self.X]] = character
                current_index += 1

    def _get_coordinates(self, current_index):
        """
        Returns the global coordinates of the character with the given index.
        E.g. the field starts at (1, 1) and the index is 2, the the resulting coordinates are (2, 1)
        :param current_index: the index of the character within this field
        :return:
        """
        pass