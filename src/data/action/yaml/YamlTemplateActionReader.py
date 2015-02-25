import yaml

from src.data.action.TemplateActionReader import TemplateActionReader


__author__ = 'DWI'


class YamlTemplateActionReader(TemplateActionReader):

    def __init__(self, action_builder):
        super(YamlTemplateActionReader, self).__init__(action_builder)

    def _load_data(self, file):
        return yaml.load(file)


    def _build_action_list(self, data):
        action_list = list()
        for field_name in data.keys():
           action = self.action_builder.build({field_name: data.get(field_name)})
           action_list.append(action)

        return action_list