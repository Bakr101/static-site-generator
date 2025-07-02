import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("div", "This is a div", [], {"class": "container"})
        self.assertEqual(repr(node), "HTMLNode(div, This is a div, [], {'class': 'container'})")
    
    def test_props_to_html(self):
        node = HTMLNode("div", "This is a div", [], {"class": "container"})
        self.assertEqual(node.props_to_html(), " class=\"container\"")
    
    def test_values(self):
        node = HTMLNode("div", "I wish I could read")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "I wish I could read")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)
    
    
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

    def test_leaf_node(self):
        node = LeafNode("div", "This is a div", {"class": "container", "id": "main", "data-id": "123"})
        self.assertEqual(node.to_html(), "<div class=\"container\" id=\"main\" data-id=\"123\">This is a div</div>")
    
    def test_leaf_node_no_tag(self):
        node = LeafNode(None, "This is a div", {"class": "container", "id": "main", "data-id": "123"})
        self.assertEqual(node.to_html(), "This is a div")
    
    def test_leaf_node_no_props(self):
        node = LeafNode("div", "This is a div", {})
        self.assertEqual(node.to_html(), "<div>This is a div</div>")
    
    def test_leaf_node_repr(self):
        node = LeafNode("div", "This is a div", {"class": "container", "id": "main", "data-id": "123"})
        self.assertEqual(repr(node), "LeafNode(div, This is a div, {'class': 'container', 'id': 'main', 'data-id': '123'})")
    
    def test_leaf_node_no_value(self):
        node = LeafNode("div", None, {"class": "container", "id": "main", "data-id": "123"})
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_parent_node(self):
        node = ParentNode("div", [LeafNode("span", "This is a span", {"class": "container", "id": "main", "data-id": "123"}), LeafNode("span", "This is a span", {"class": "container", "id": "main", "data-id": "123"})], {"class": "container", "id": "main", "data-id": "123"})
        self.assertEqual(node.to_html(), "<div class=\"container\" id=\"main\" data-id=\"123\"><span class=\"container\" id=\"main\" data-id=\"123\">This is a span</span><span class=\"container\" id=\"main\" data-id=\"123\">This is a span</span></div>")
    
    def test_parent_node_no_tag(self):
        parent = ParentNode(None, [LeafNode("span", "This is a span", {"class": "container", "id": "main", "data-id": "123"}), LeafNode("span", "This is a span", {"class": "container", "id": "main", "data-id": "123"})], {"class": "container", "id": "main", "data-id": "123"})
        with self.assertRaises(ValueError):
            parent.to_html()
    
    def test_parent_node_no_children(self):
        parent = ParentNode("div", None, {"class": "container", "id": "main", "data-id": "123"})
        with self.assertRaises(ValueError):
            parent.to_html()
    
    def test_parent_node_multiple_children(self):
        node = ParentNode("div", [LeafNode("span", "This is a span", {"class": "container", "id": "main", "data-id": "123"}), LeafNode("span", "This is a span", {"class": "container", "id": "main", "data-id": "123"}), LeafNode("span", "This is a span", {"class": "container", "id": "main", "data-id": "123"}), LeafNode("span", "This is a span", {"class": "container", "id": "main", "data-id": "123"}), LeafNode("span", "This is a span", {"class": "container", "id": "main", "data-id": "123"})], {"class": "container", "id": "main", "data-id": "123"})
        self.assertEqual(node.to_html(), "<div class=\"container\" id=\"main\" data-id=\"123\"><span class=\"container\" id=\"main\" data-id=\"123\">This is a span</span><span class=\"container\" id=\"main\" data-id=\"123\">This is a span</span><span class=\"container\" id=\"main\" data-id=\"123\">This is a span</span><span class=\"container\" id=\"main\" data-id=\"123\">This is a span</span><span class=\"container\" id=\"main\" data-id=\"123\">This is a span</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node], {"class": "container", "id": "main", "data-id": "123"})
        parent_node = ParentNode("div", [child_node], {"class": "container", "id": "main", "data-id": "123"})
        self.assertEqual(
            parent_node.to_html(),
            "<div class=\"container\" id=\"main\" data-id=\"123\"><span class=\"container\" id=\"main\" data-id=\"123\"><b>grandchild</b></span></div>",
        )
    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
    
    

if __name__ == "__main__":
    unittest.main()