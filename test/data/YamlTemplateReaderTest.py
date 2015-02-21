from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.isequal import equal_to
from hamcrest.library.object import has_property

from src.data.yaml.YamlTemplateReader import YamlTemplateReader
from src.data.yaml.YamlTemplateFieldBuilder import YamlTemplateFieldBuilder


__author__ = 'DWI'

import unittest


class YamlTemplateReaderTest(unittest.TestCase):
    def test_read_template(self):
        reader = YamlTemplateReader(YamlTemplateFieldBuilder())
        template = reader.read("./template.yaml")

        assert_that(template.field_list[0], has_property("name", equal_to("foo")))
        assert_that(template.name, equal_to("test"))


if __name__ == '__main__':
    unittest.main()

