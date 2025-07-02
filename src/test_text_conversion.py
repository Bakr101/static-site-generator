import unittest
from textnode import TextNode, TextType
from text_conversion import split_nodes_by_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes

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

    def test_extract_markdown_images(self):
        text = "This is a test image ![test](https://www.boot.dev)"
        self.assertEqual(extract_markdown_images(text), [("test", "https://www.boot.dev")])

    def test_extract_markdown_images_multiple(self):
        text = "This is a test image ![test](https://www.boot.dev) and ![test2](https://www.boot.dev/2)"
        self.assertEqual(extract_markdown_images(text), [("test", "https://www.boot.dev"), ("test2", "https://www.boot.dev/2")])
    
    def test_extract_markdown_images_no_match(self):
        text = "This is a test image"
        self.assertEqual(extract_markdown_images(text), None)
    
    def test_extract_markdown_links(self):
        text = "This is a test link [test](https://www.boot.dev)"
        self.assertEqual(extract_markdown_links(text), [("test", "https://www.boot.dev")])
    
    def test_extract_markdown_links_multiple(self):
        text = "This is a test link [test](https://www.boot.dev) and [test2](https://www.boot.dev/2)"
        self.assertEqual(extract_markdown_links(text), [("test", "https://www.boot.dev"), ("test2", "https://www.boot.dev/2")])
    
    def test_extract_markdown_links_no_match(self):
        text = "This is a test link"
        self.assertEqual(extract_markdown_links(text), None)
    
    def test_split_nodes_image(self):
        node = TextNode("This is a test image ![test](https://www.boot.dev)", TextType.NORMAL)
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes, [TextNode("This is a test image ", TextType.NORMAL), TextNode("test", TextType.IMAGE, "https://www.boot.dev")])
    
    def test_split_nodes_link(self):
        node = TextNode("This is a test link [test](https://www.boot.dev)", TextType.NORMAL)
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes, [TextNode("This is a test link ", TextType.NORMAL), TextNode("test", TextType.LINK, "https://www.boot.dev")])
    
    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and ", TextType.NORMAL),
                TextNode("another link", TextType.LINK, "https://blog.boot.dev"),
                TextNode(" with text that follows", TextType.NORMAL),
            ],
            new_nodes,
        )
    
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.NORMAL),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.NORMAL),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        self.assertEqual(text_to_textnodes(text), [TextNode("This is ", TextType.NORMAL), TextNode("text", TextType.BOLD), TextNode(" with an ", TextType.NORMAL), TextNode("italic", TextType.ITALIC), TextNode(" word and a ", TextType.NORMAL), TextNode("code block", TextType.CODE), TextNode(" and an ", TextType.NORMAL), TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"), TextNode(" and a ", TextType.NORMAL), TextNode("link", TextType.LINK, "https://boot.dev")])
    
    def test_text_to_textnodes_new_case(self):
        text = "This is *ahmed* and his friend **ali** this is his code `print('hello')` and this is their image ![ahmed & ali](https://i.imgur.com/fJRm4Vk.jpeg) and this is their website link [ahmed & ali](https://ahmed.com)"
        self.assertEqual(text_to_textnodes(text), [TextNode("This is ", TextType.NORMAL), TextNode("ahmed", TextType.ITALIC), TextNode(" and his friend ", TextType.NORMAL), TextNode("ali", TextType.BOLD), TextNode(" this is his code ", TextType.NORMAL), TextNode("print('hello')", TextType.CODE), TextNode(" and this is their image ", TextType.NORMAL), TextNode("ahmed & ali", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"), TextNode(" and this is their website link ", TextType.NORMAL), TextNode("ahmed & ali", TextType.LINK, "https://ahmed.com")])

if __name__ == "__main__":
    unittest.main()