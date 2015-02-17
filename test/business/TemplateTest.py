from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.isequal import equal_to
from src.vo.template.RectangularTemplateField import RectangularTemplateField
from src.vo.template.Template import Template

__author__ = 'DWI'

import unittest


class MyTestCase(unittest.TestCase):
    def test_render(self):
        image = "123 yxz 123\n234 abc 234"
        upper_field = RectangularTemplateField("one",(4, 0), (6, 0))
        lower_field = RectangularTemplateField("two",(4, 1), (6, 1))
        upper_field.value = "foo"
        lower_field.value = "bar"
        template = Template(image, [upper_field, lower_field])

        assert_that( template.render(), equal_to("123 foo 123\n234 bar 234"))


if __name__ == '__main__':
    unittest.main()
