from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.isequal import equal_to
from hamcrest.library.object import has_property
from src.data.TemplateFieldBuilder import TemplateFieldBuilder
from src.data.TemplateReader import TemplateReader
from src.data.YamlTemplateFieldBuilder import YamlTemplateFieldBuilder
from src.data.YamlTemplateReader import YamlTemplateReader

__author__ = 'DWI'

import unittest



class TemplateReaderTest(unittest.TestCase):
    def test_read_template(self):
        reader = YamlTemplateReader(YamlTemplateFieldBuilder())
        template = reader.read("./template.yaml")

        assert_that(template.field_list[0], has_property("name", equal_to("foo")))


if __name__ == '__main__':
    unittest.main()

