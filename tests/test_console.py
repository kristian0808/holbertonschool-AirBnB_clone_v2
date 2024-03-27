import unittest
from unittest.mock import patch
from io import StringIO
import sys
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit_command(self, mock_stdout):
        with patch('sys.stdin', StringIO('quit\n')):
            HBNBCommand().cmdloop()
        self.assertEqual(mock_stdout.getvalue(), '(hbnb) Exiting HBNBCommand...\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_command(self, mock_stdout):
        with patch('sys.stdin', StringIO('create BaseModel\nquit\n')):
            HBNBCommand().cmdloop()
        self.assertIn('hbnb', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_command(self, mock_stdout):
        with patch('sys.stdin', StringIO('show BaseModel\nquit\n')):
            HBNBCommand().cmdloop()
        self.assertIn('** instance id missing **', mock_stdout.getvalue())

    # Add more tests for other commands...

if __name__ == '__main__':
    unittest.main()
