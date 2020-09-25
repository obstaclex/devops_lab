from unittest import TestCase
import handlers.pulls
from tests.variables import template, full, open_label, closed_label, accepted, needs_work


class FlaskApp(TestCase):
    """Tests for flask app"""

    def test_parse_json(self):
        """Test for parse json"""
        self.assertEqual(handlers.pulls.parse_json(template), full)

    def test_parse_json_state(self):
        """Test for parse based on state"""
        self.assertEqual(handlers.pulls.parse_json_state("open", template), open_label)
        self.assertEqual(handlers.pulls.parse_json_state("closed", template), closed_label)

    def test_parse_json_label(self):
        """Test for parse based on label"""
        self.assertEqual(handlers.pulls.parse_json_label("accepted", template), accepted)
        self.assertEqual(handlers.pulls.parse_json_label("needs work", template), needs_work)
