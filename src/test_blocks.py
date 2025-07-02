import unittest
from blocks import markdown_to_blocks, blocks_to_block_type, BlockType

class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        self.assertEqual(markdown_to_blocks("This is a test"), ["This is a test"])
    def test_markdown_to_blocks_with_new_line(self):
        self.assertEqual(markdown_to_blocks(
            """
            # This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""),
[
    "# This is a heading",
    "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
    """* This is the first list item in a list block
* This is a list item
* This is another list item""",
])

    def test_markdown_to_blocks_newlines2(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )
def test_blocks_to_block_type(self):
    self.assertEqual(blocks_to_block_type("This is a paragraph"), BlockType.PARAGRAPH)
def test_blocks_to_block_type_heading(self):
    self.assertEqual(blocks_to_block_type("# This is a heading"), BlockType.HEADING_1)
def test_blocks_to_block_type_list(self):
    self.assertEqual(blocks_to_block_type("* This is a list item"), BlockType.UNORDERED_LIST)
def test_blocks_to_block_type_ordered_list(self):
    self.assertEqual(blocks_to_block_type("1. This is an ordered list item"), BlockType.ORDERED_LIST)

if __name__ == "__main__":
    unittest.main()
