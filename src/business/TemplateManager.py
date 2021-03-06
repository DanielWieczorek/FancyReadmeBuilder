"""
Module for TemplateManager
"""
import os

from src.data.InputFileType import InputFileType


__author__ = 'DWI'


class TemplateManager(object):
    """
    Class that can read all templates from directories into an internal dictionary for later use
    """

    def __init__(self, template_reader_factory):
        self._template_reader_factory = template_reader_factory
        self._templates = dict()

    def load_templates(self, directory):
        """
        Loads all templates from the given directory. The file extension has
        to be the TemplateType. This function is not recursive.
        :param directory: the path to the directory to read all templates from
        """
        for template_file in os.listdir(directory):
            file_extension = os.path.splitext(template_file)[1]
            if file_extension:
                file_extension = file_extension[1:]
                try:
                    reader_type = InputFileType[file_extension]
                    reader = self._template_reader_factory.build_for_type(reader_type)
                    template = reader.read(os.path.join(directory, template_file))
                    self._templates[template.name] = template
                except KeyError:
                    print("type not supported")

    def get_template(self, template_name):
        return self._templates.get(template_name)