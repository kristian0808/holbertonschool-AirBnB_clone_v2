import unittest
from unittest.mock import patch
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.hbnb_cmd = HBNBCommand()

    def test_prompt(self):
        self.assertEqual(self.hbnb_cmd.prompt, '(hbnb) ')

    def test_precmd(self):
        line = 'create BaseModel'
        new_line = self.hbnb_cmd.precmd(line)
        self.assertEqual(new_line, 'create BaseModel')

    def test_do_quit(self):
        with self.assertRaises(SystemExit):
            self.hbnb_cmd.do_quit(None)

    @patch('builtins.print')
    def test_help_quit(self, mock_print):
        self.hbnb_cmd.help_quit()
        mock_print.assert_called_with("Exits the program with formatting\n")

    def test_do_EOF(self):
        with patch('sys.exit') as mock_exit:
            self.hbnb_cmd.do_EOF(None)
            mock_exit.assert_called_once()

    @patch('builtins.print')
    def test_help_EOF(self, mock_print):
        self.hbnb_cmd.help_EOF()
        mock_print.assert_called_with("Exits the program without formatting\n")

    def test_emptyline(self):
        self.assertIsNone(self.hbnb_cmd.emptyline())

    def test_key_value_parser(self):
        args = ['name="John"', 'age=25', 'is_active=True']
        result = self.hbnb_cmd._key_value_parser(args)
        expected_result = {'name': 'John', 'age': 25, 'is_active': True}
        self.assertEqual(result, expected_result)

    @patch('builtins.print')
    def test_do_create(self, mock_print):
        with patch.object(HBNBCommand.classes['BaseModel'],
                          'save') as mock_save:
            self.hbnb_cmd.do_create
            ('BaseModel name="test" age=20 is_active=True')
            mock_save.assert_called_once()
            mock_print.assert_called_with(mock_save().id)


if __name__ == '__main__':
    unittest.main()
