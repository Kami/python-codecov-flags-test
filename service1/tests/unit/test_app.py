import sys
import unittest

from src.app import to_lowercase


class AppTestCase(unittest.TestCase):
    def test_to_lowercase(self):
        value = to_lowercase('FOO')
        self.assertEqual(value, 'foo')
        self.assertEqual(to_lowercase(''), None)
