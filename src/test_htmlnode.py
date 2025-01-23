import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("div", "This is a div", [], {"class": "container"})
        self.assertEqual(repr(node), "HTMLNode(div, This is a div, [], {'class': 'container'})")
    
    def test_props_to_html(self):
        node = HTMLNode("div", "This is a div", [], {"class": "container"})
        self.assertEqual(node.props_to_html(), " class=\"container\"")
    
    def test_eq(self):
        node = HTMLNode("div", "This is a div", [], {"class": "container"})
        node2 = HTMLNode("div", "This is a div", [], {"class": "container"})
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = HTMLNode("div", "This is a div", [], {"class": "container"})
        node2 = HTMLNode("div", "This is a div", [], {"class": "container2"})
        self.assertNotEqual(node, node2)
    def test_multiple_props(self):
        node = HTMLNode("div", "This is a div", [], {"class": "container", "id": "main", "data-id": "123"})
        self.assertEqual(node.props_to_html(), " class=\"container\" id=\"main\" data-id=\"123\"")

if __name__ == "__main__":
    unittest.main()