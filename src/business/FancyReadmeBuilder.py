"""
Module for FancyReadmeBuilder
"""
import os

from src.business.TemplateManager import TemplateManager

from src.data.InputFileType import InputFileType
from src.data.action.TemplateActionReaderFactory import TemplateActionReaderFactory
from src.data.template.TemplateReaderFactory import TemplateReaderFactory


__author__ = 'DWI'


class FancyReadmeBuilder():
    """
    The main class of the fancy readme builder.

    First load the templates from a directory and then apply
    the actions from a configuration file and render the result
    """

    def __init__(self, template_manager, action_reader_factory):
        self._template_manager = template_manager
        self._action_reader_factory = action_reader_factory

    def load_templates(self, directory):
        """
        Loads all templates from a given directory.

        This function is only a facade for the corresponding function of
        a TemplateManager object.
        :param directory: name of the directory to read the template files from
        """
        self._template_manager.load_templates(directory)

    def read_actions(self, actions_file):
        """
        reads all actions from a given file. The file has to be parseable.
        How it is parsed is determined by the file ending.
        :param actions_file: file containing the actions.
        :return: a list of actions read from the file
        """
        file_extension = os.path.splitext(actions_file)[1]
        if file_extension:
                file_extension = file_extension[1:]
                try:
                    reader_type = InputFileType[file_extension]
                    reader = self._action_reader_factory.build_for_type(reader_type)
                    return reader.read(actions_file)
                except KeyError:
                    print("type not supported")
        return None

    def apply_actions_and_render(self, action_file, template_name):
        """
        Reads the actions from the file, applies them to the given template and returns the rendered result.
        :param action_file: the file containing the action descriptions
        :param template_name: the name of the template
        :return: string containing the rendered result
        """
        template = self._template_manager.get_template(template_name)
        for action in self.read_actions(action_file):
            action.apply_to(template)

        return template.render()

    @staticmethod
    def get_instance():
        """

        :return: Returns a ready to use instance of this class.
        """
        return FancyReadmeBuilder(TemplateManager(TemplateReaderFactory()),TemplateActionReaderFactory())