from textnode import TextNode, TextType
from text_conversion import split_nodes_by_delimiter
def main():
    # bold = TextType.BOLD_TEXT
    # text_node = TextNode("This is a text node", bold, "https://www.boot.dev")
    # print(text_node)
    node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.NORMAL
        )
    new_nodes = split_nodes_by_delimiter([node], "**", TextType.BOLD)
    print(new_nodes)

main()
