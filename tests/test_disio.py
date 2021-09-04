import unittest

from disio import __version__


class Toaster(unittest.TestCase):
    """Useless tests for disio."""

    def test_version(self):
        self.assertEqual(__version__, "0.1.0")
