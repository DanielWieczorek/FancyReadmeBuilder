__author__ = 'DWI'


class TemplateActionReader(object):

    def __init__(self, template_action_builder):
        self.action_builder = template_action_builder

    def read(self, file_name):
        """
        Reads the given file and returns a template object
        :param file_name: name of the template file
        :return: the template that was created
        """
        with open(file_name, 'r') as file:
            data = self._load_data(file)
        return self._build_action_list(data)



    def _build_action_list(self, data):
        pass

    def _load_data(self, file):
        pass