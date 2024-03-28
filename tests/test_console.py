import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models import storage


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        """Set up the test case environment."""
        self.console = HBNBCommand()

    def test_prompt(self):
        """Test the prompt attribute."""
        self.assertEqual(self.console.prompt, "(hbnb) ")

    def test_emptyline(self):
        """Test the emptyline method does nothing."""
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.console.onecmd("\n")
            self.assertEqual(fake_output.getvalue(), "")

    def test_quit(self):
        """Test the quit command exits the program."""
        with self.assertRaises(SystemExit):
            self.console.onecmd("quit")

    def test_create(self):
        """Test object creation."""
        with patch("sys.stdout", new=StringIO()) as fake_output:
            with patch("models.storage") as mock_storage:
                mock_storage.new = unittest.mock.MagicMock()
                self.console.onecmd("create BaseModel")
                mock_storage.new.assert_called()
                # Further assertions can be made based on the expected behavior

    # Add more tests for other commands and functionalities as needed


if __name__ == "__main__":
    unittest.main()
