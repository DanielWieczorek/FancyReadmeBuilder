from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.isequal import equal_to

from src.business.TemplateManager import TemplateManager
from src.data.template.TemplateReaderFactory import TemplateReaderFactory


__author__ = 'DWI'

import unittest


class TemplateManagerTest(unittest.TestCase):
    def test_get_template(self):

        reader_factory = TemplateReaderFactory()
        manager = TemplateManager(reader_factory)
        directory = "./templates"
        manager.load_templates(directory)
        assert_that(manager._templates.get("test").render(), equal_to("123"))
        assert_that(manager._templates.get("test2").render(), equal_to("123"))


if __name__ == '__main__':
    unittest.main()
