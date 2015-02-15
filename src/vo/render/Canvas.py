__author__ = 'DWI'


class Canvas(object):

    def __init__(self, background_string):
        self.data_matrix = background_string.split("\n")
        for i in range(len(self.data_matrix)):
            self.data_matrix[i] = list(self.data_matrix[i])

    def draw(self, template_field):
        template_field.draw_onto(self)

    def get_string(self):
        result = ""
        for line in self.data_matrix:
            result += "".join(line)
        return result
