from textnode import TextNode, TextType
def main():
    bold = TextType.BOLD_TEXT
    text_node = TextNode("This is a text node", bold, "https://www.boot.dev")
    print(text_node)

main()
