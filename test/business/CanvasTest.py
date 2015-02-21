from src.model.render.Canvas import Canvas
from src.model.template.RectangularTemplateField import RectangularTemplateField

__author__ = 'DWI'
from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.isequal import equal_to
import unittest


class CanvasTest(unittest.TestCase):
    def test_draw_single_line(self):

        field = RectangularTemplateField("name", (4, 0), (6, 0))
        field.value = "foo"
        canvas = Canvas("123 xxx 123")
        canvas.draw(field)
        assert_that(canvas.get_string(), equal_to("123 foo 123"))

    def test_draw_multi_line(self):

        field = RectangularTemplateField("name", (4, 0), (6, 1))
        field.value = "foobar"
        canvas = Canvas("123 xxx 123\n123 xxx 123")
        canvas.draw(field)
        assert_that(canvas.get_string(), equal_to("123 foo 123\n123 bar 123"))


if __name__ == '__main__':
    unittest.main()
