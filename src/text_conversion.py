from textnode import TextNode, TextType

def split_nodes_by_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    result = []
    for old_node in old_nodes:
        if old_node.text_type != text_type.NORMAL:
            result.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for idx in range(len(sections)):
            if sections[idx] == "":
                continue
            if idx % 2 == 0:
                split_nodes.append(TextNode(sections[idx], TextType.NORMAL))
            else:
                split_nodes.append(TextNode(sections[idx], text_type))
        result.extend(split_nodes)
    return result
