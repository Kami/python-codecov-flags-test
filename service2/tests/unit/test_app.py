import sys
import unittest

from src.app import to_lowercase
from src.app import to_uppercase


class AppTestCase(unittest.TestCase):
    def test_to_lowercase(self):
        value = to_lowercase('FOO')
        self.assertEqual(value, 'foo')

    def test_to_uppercase(self):
        value = to_uppercase('foo')
        self.assertEqual(value, 'FOO')
