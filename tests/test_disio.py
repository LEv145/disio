import unittest

from disio import __version__


class Toster(unittest.TestCase):
    """Class for tests"""
    def test_version(self):
        self.assertEqual(__version__, "0.1.0")
