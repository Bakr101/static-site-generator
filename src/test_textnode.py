import unittest

from textnode import TextNode, TextType, text_node_to_html_node


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


class TestTextNodeToHTMLNode(unittest.TestCase):    
    def test_text_node_to_html_node(self):
        node = text_node_to_html_node(TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev"))
        self.assertEqual(node.to_html(), "<b>This is a text node</b>")
    
    def test_text_node_to_html_node_normal(self):
        node = text_node_to_html_node(TextNode("This is a text node", TextType.NORMAL))
        self.assertEqual(node.to_html(), "This is a text node")
    
    def test_text_node_to_html_node_italic(self):
        node = text_node_to_html_node(TextNode("This is a text node", TextType.ITALIC))
        self.assertEqual(node.to_html(), "<i>This is a text node</i>")
    
    def test_text_node_to_html_node_code(self):
        node = text_node_to_html_node(TextNode("This is a text node", TextType.CODE))
        self.assertEqual(node.to_html(), "<code>This is a text node</code>")
    
    def test_text_node_to_html_node_link(self):
        node = text_node_to_html_node(TextNode("This is a text node", TextType.LINK, "https://www.boot.dev"))
        self.assertEqual(node.to_html(), "<a href=\"https://www.boot.dev\">This is a text node</a>")
    
    def test_text_node_to_html_node_image(self):
        node = text_node_to_html_node(TextNode("This is a text node", TextType.IMAGE, "https://www.boot.dev"))
        self.assertEqual(node.to_html(), "<img src=\"https://www.boot.dev\" alt=\"This is a text node\"></img>")
    
    def test_text_node_to_html_fail(self):
        with self.assertRaises(ValueError):
            text_node_to_html_node(TextNode("This is a text node", "TextType.LINK", "https://www.boot.dev")) # Invalid because it is a string

    def test_text(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")
    

if __name__ == "__main__":
    unittest.main()