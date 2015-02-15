__author__ = 'DWI'


class TemplateField(object):
    X = 0
    Y = 1

    def __init__(self, name, start_point, end_point):
        self.name = name
        self.value = None
        self.start_point = start_point
        self.end_point = end_point

    def get_size(self):
        pass

    def __iter__(self):
        return self

    def draw_onto(self, canvas):
        canvas_data = canvas.data_matrix
        current_index = 0
        if self.value is not None:
            for character in self.value:
                coordinates = self._get_coordinates(current_index)
                canvas_data[coordinates[self.Y]][coordinates[self.X]] = character
                current_index += 1

    def _get_coordinates(self, current_index):
        pass