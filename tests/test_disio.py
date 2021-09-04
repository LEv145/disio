import unittest

from disio import __version__


class Toster(unittest.TestCase):
    """Class for tests"""
    def test_version(self):
        """Checks the bot version for equivalence"""
        self.assertEqual(__version__, "0.1.0")
