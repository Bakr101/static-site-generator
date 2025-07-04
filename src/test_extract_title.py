import unittest

from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        self.assertEqual(extract_title("# Hello, world!"), "Hello, world!")
        self.assertEqual(extract_title("# Hello, world!\n\nThis is a description"), "Hello, world!")
        self.assertEqual(extract_title("# Hello, world!\n\nThis is a description \n\n### this is a subheading"), "Hello, world!")
        self.assertEqual(extract_title("# Hello, world!\n\nThis is a description \n\n## this is a subheading"), "Hello, world!")