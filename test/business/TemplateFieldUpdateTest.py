from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.isequal import equal_to

from src.vo.template.RectangularTemplateField import RectangularTemplateField
from src.vo.template.Template import Template
from src.vo.action.TemplateFieldUpdate import TemplateFieldUpdate


__author__ = 'DWI'

import unittest


class TemplateFieldUpdateTest(unittest.TestCase):
    def test_apply_positive(self):
        template_image = "== 12345 =="
        template_field = RectangularTemplateField("foo", (0, 4), (0, 8))
        template = Template(template_image, template_field,"template_name")

        TemplateFieldUpdate("foo", "Hello").apply_to(template)

        assert_that(template_field.value, equal_to("Hello"))

    def test_apply_positive_too_long(self):
        template_image = "== 12345 =="
        template_field = RectangularTemplateField("foo", (0, 4), (0, 8))
        template = Template(template_image, template_field, "template_name")

        TemplateFieldUpdate("foo", "Hello0000").apply_to(template)

        assert_that(template_field.value, equal_to("Hello"))

    def test_apply_multi_line(self):
        template_image = "== 12345 ===\n== 12345 ==="
        template_field = RectangularTemplateField("foo", (0, 4), (1, 8))
        template = Template(template_image, template_field, "template_name")

        TemplateFieldUpdate("foo", "Hello00000").apply_to(template)

        assert_that(template_field.value, equal_to("Hello00000"))


if __name__ == '__main__':
    unittest.main()
