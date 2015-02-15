__author__ = 'DWI'

X = 0
Y = 1


class TemplateField(object):

    def __init__(self, name, start_point, end_point):
        self.name = name
        self.value = None
        self.start_point = start_point
        self.end_point = end_point

    def get_size(self):
        return (self.end_point[X] - self.start_point[X] + 1) * (self.end_point[Y] - self.start_point[Y] + 1)

    def __iter__(self):
        return self
