"""
Module for YamlTemplateFieldBuilder
"""

__author__ = 'DWI'


class TemplateReader(object):
    """
    Class for reading complete Templates from files.
    """

    def __init__(self, template_field_builder):
        self.field_builder = template_field_builder

    def read(self, file_name):
        """
        Reads the given file and returns a template object
        :param file_name: name of the template file
        :return: the template that was created
        """
        with open(file_name, 'r') as file:
            data = self._load_data(file)
        return self._build_template(data)

    def _load_data(self, file):
        pass

    def _build_template(self, template_data):
        pass


    def _load_background_image(self, file_name):
        """
        Reads the background image from the given file
        :param file_name: name of the file to read the data from
        :return: the content of the file as string
        """
        with open(file_name, "r") as file:
            return file.read()