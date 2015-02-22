from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.isequal import equal_to
from hamcrest.library.object import has_property

from src.data.TemplateReaderType import TemplateReaderType
from src.data.TemplateReaderFactory import TemplateReaderFactory


__author__ = 'DWI'

import unittest


class YamlTemplateReaderTest(unittest.TestCase):
    def test_read_template(self):
        reader_factory = TemplateReaderFactory()
        reader = reader_factory.build_for_type(TemplateReaderType.yaml)
        template = reader.read("./templates/template.yaml")

        assert_that(template.field_list[0], has_property("name", equal_to("foo")))
        assert_that(template.name, equal_to("test"))
        assert_that(template.render(), equal_to("1234"))

if __name__ == '__main__':
    unittest.main()

