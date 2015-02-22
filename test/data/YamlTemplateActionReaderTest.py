from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.isequal import equal_to
from hamcrest.library.collection import has_item
from hamcrest.library.object import has_properties

from src.data.InputFileType import InputFileType
from src.data.action.TemplateActionReaderFactory import TemplateActionReaderFactory


__author__ = 'DWI'

import unittest


class YamlTemplateActionReaderTest(unittest.TestCase):
    def test_read_action_file(self):
        reader_factory = TemplateActionReaderFactory()
        action_reader = reader_factory.build_for_type(InputFileType.yaml)
        actions = action_reader.read("./actions/actions.yaml")


        assert_that(actions, has_item(has_properties({"value":"hello world", "field_name":"foo"})))
        assert_that(actions, has_item(has_properties({"value":"hello world2", "field_name":"bar"})))
        assert_that(len(actions), equal_to(2))


if __name__ == '__main__':
    unittest.main()
