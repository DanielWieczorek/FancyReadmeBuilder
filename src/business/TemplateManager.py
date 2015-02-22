import os

from src.data.TemplateReaderType import TemplateReaderType


__author__ = 'DWI'


class TemplateManager():

    def __init__(self,template_reader_factory):
        self._template_reader_factory = template_reader_factory
        self._templates = dict()



    def load_templates(self, directory):
        for template_file in os.listdir(directory):
            file_extension = template_file[template_file.rindex(".")+1:]
            reader = self._template_reader_factory.build_for_type(TemplateReaderType[file_extension])
            template = reader.read(os.path.join(directory,template_file))
            self._templates[template.name] = template

