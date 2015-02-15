__author__ = 'DWI'


class Template():

    def __init__(self, image, fields):
        self._image = image
        self.field_list = list()
        self.field_list.append(fields)

    def __iter__(self):
        return iter(self.field_list)