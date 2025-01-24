import unittest
from textnode import TextNode, TextType
from delimiter import split_nodes_by_delimiter

class TestDelimiter(unittest.TestCase):
    def test_split_nodes_by_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        new_nodes = split_nodes_by_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.NORMAL), TextNode("code block", TextType.CODE), TextNode(" word", TextType.NORMAL)])
    
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.NORMAL)
        new_nodes = split_nodes_by_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.NORMAL),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.NORMAL
        )
        new_nodes = split_nodes_by_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.NORMAL),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )
        
    def test_delim_italic(self):    
        node = TextNode("This is text with a *italic* word", TextType.NORMAL)
        new_nodes = split_nodes_by_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            [TextNode("This is text with a ", TextType.NORMAL), TextNode("italic", TextType.ITALIC), TextNode(" word", TextType.NORMAL)],
            new_nodes,
        )
    
    def test_delim_code(self):
        node = TextNode("This is text with a `code` word", TextType.NORMAL)
        new_nodes = split_nodes_by_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [TextNode("This is text with a ", TextType.NORMAL), TextNode("code", TextType.CODE), TextNode(" word", TextType.NORMAL)],
            new_nodes,
        )

    
if __name__ == "__main__":
    unittest.main()