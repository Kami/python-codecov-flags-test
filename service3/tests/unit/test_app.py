import sys
import unittest

from src.app import to_lowercase
from src.app import to_uppercase
from src.app import trim


class AppTestCase(unittest.TestCase):
    def test_to_lowercase(self):
        value = to_lowercase('FOO')
        self.assertEqual(value, 'foo')

    def test_to_uppercase(self):
        value = to_uppercase('foo')
        self.assertEqual(value, 'FOO')

    def test_trim(self):
        value = trim('abcd    ')
        self.assertEqual(value, 'abcd')
