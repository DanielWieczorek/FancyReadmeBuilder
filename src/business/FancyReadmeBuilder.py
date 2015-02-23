import os

from src.data.InputFileType import InputFileType


__author__ = 'DWI'


class FancyReadmeBuilder():

    def __init__(self, template_manager, action_reader_factory):
        self._template_manager = template_manager
        self._action_reader_factory = action_reader_factory


    def load_templates(self, directory):
        self._template_manager.load_templates(directory)

    def read_actions(self, actions_file):
        file_extension = os.path.splitext(actions_file)[1]
        if file_extension:
                file_extension = file_extension[1:]
                try:
                    reader_type = InputFileType[file_extension]
                    reader = self._action_reader_factory.build_for_type(reader_type)
                    return reader.read(actions_file)
                except KeyError:
                    print("type not supported")

    def apply_actions_and_render(self, action_file, template_name):
        template = self._template_manager.get_template(template_name)
        for action in self.read_actions(action_file):
            action.apply_to(template)

        return template.render()

    @staticmethod
    def get_instance():
        pass