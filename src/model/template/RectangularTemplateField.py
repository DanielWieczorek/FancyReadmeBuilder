"""
Module for RectangularTemplateField
"""
from src.model.template.TemplateField import TemplateField

__author__ = 'DWI'


class RectangularTemplateField(TemplateField):
    """
    Class representing a rectangular template field.
    """

    def __init__(self, name, start_point, end_point):
        super(RectangularTemplateField, self).__init__(name, start_point, end_point)

    def get_size(self):
        """
        Calculates the size of this TemplateField by multiplying height and width
        :return: the size of this field in characters
        """
        height = (self.end_point[self.Y] - self.start_point[self.Y] + 1)
        width = (self.end_point[self.X] - self.start_point[self.X] + 1)
        return height * width

    def _get_coordinates(self, current_index):
        x_coordinate = current_index % self._get_width() + self.start_point[self.X]
        y_coordinate = current_index // self._get_width() + self.start_point[self.Y]
        return x_coordinate, y_coordinate

    def _get_width(self):
        return self.end_point[self.X] - self.start_point[self.X] + 1

    def _get_height(self):
        return self.end_point[self.Y] - self.start_point[self.Y] + 1