import unittest
from unittest.mock import patch
from io import StringIO
import sys

from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_quit(self, mock_stdout):
        self.console.onecmd('help quit')
        self.assertEqual(mock_stdout.getvalue().strip(),
                         "Exits the program with formatting")

    # Add more test methods for other commands...


if __name__ == '__main__':
    unittest.main()
