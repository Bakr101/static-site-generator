import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.NORMAL)
        self.assertNotEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, None)")
    
    def test_repr_with_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, https://www.boot.dev)")

    def test_repr_with_image(self):
        node = TextNode("This is a text node", TextType.IMAGE, "https://www.boot.dev")
        self.assertEqual(repr(node), "TextNode(This is a text node, image, https://www.boot.dev)")

if __name__ == "__main__":
    unittest.main()