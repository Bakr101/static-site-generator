from enum import Enum
from htmlnode import LeafNode, ParentNode, HTMLNode
from textnode import TextNode, TextType, text_node_to_html_node
from text_conversion import text_to_textnodes

def markdown_to_blocks(markdown: str) -> list[str]:
    split_markdown = markdown.split("\n\n")
    blocks = []
    for block in split_markdown:
      block = block.strip()
      if block == "":
         continue
      blocks.append(block)
    return blocks

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING_1 = "heading_1"
    HEADING_2 = "heading_2"
    HEADING_3 = "heading_3"
    HEADING_4 = "heading_4"
    HEADING_5 = "heading_5"
    HEADING_6 = "heading_6"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block: str) -> BlockType:
    lines = block.split("\n")
    #check if it's a heading
    if block.startswith("#"):
       #which heading level
       heading_level = 0
       for char in block:
           if char == "#":
               heading_level += 1
           else:
               break
       return BlockType[f"HEADING_{heading_level}"]
    #check if it's a code block
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    #check if it's a quote & valid
    if block.strip().startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
              
    #check if it's an unordered list & valid
    if block.startswith("*") or block.startswith("-"):
        for line in lines:
            if not (line.startswith("*") or line.startswith("-")):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
       
    #check if it's an ordered list & valid
    if block.startswith("1. "):
        valid_list_lines = 0
        for line in lines:
            if not line.startswith(f"{valid_list_lines+1}. "):
                return BlockType.PARAGRAPH
            valid_list_lines += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown: str) -> HTMLNode:
    #split markdown to blocks
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)
        
    


def block_to_html_node(block: str) -> HTMLNode:
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    elif block_type == BlockType.HEADING_1 or block_type == BlockType.HEADING_2 or block_type == BlockType.HEADING_3 or block_type == BlockType.HEADING_4 or block_type == BlockType.HEADING_5 or block_type == BlockType.HEADING_6:
        return heading_to_html_node(block, block_type)
    elif block_type == BlockType.CODE:
        return code_to_html_node(block)
    elif block_type == BlockType.QUOTE:
        return blockquote_to_html_node(block)
    elif block_type == BlockType.UNORDERED_LIST:
        return ul_to_html_node(block)
    elif block_type == BlockType.ORDERED_LIST:
        return ol_to_html_node(block)
    raise ValueError(f"Invalid block type: {block_type}")
    

def text_to_children(text: str):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def paragraph_to_html_node(block: str) -> ParentNode:
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)
    

def heading_to_html_node(block: str, block_type: BlockType) -> ParentNode:
    heading_level = block_type.value.split("_")[1]
    heading_text = block.lstrip("#").strip()
    children = text_to_children(heading_text)
    return ParentNode(f"h{heading_level}", children)


def blockquote_to_html_node(block: str) -> HTMLNode:
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid blockquote")
        line = line.lstrip(">").strip()
        new_lines.append(line)
    full_text = " ".join(new_lines)
    children = text_to_children(full_text)
    return ParentNode("blockquote", children)


            
def code_to_html_node(block: str) -> ParentNode:
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    raw_code = block[4:-3]
    raw_text_node = TextNode(raw_code, TextType.NORMAL)
    child = text_node_to_html_node(raw_text_node)
    code_tag = ParentNode("code", [child])
    return ParentNode("pre", [code_tag])

def ul_to_html_node(block: str) -> ParentNode:
    list_lines = block.split("\n")
    list_items = []
    for line in list_lines:
        line_without_prefix = line[2:]
        children = text_to_children(line_without_prefix)
        list_items.append(ParentNode("li", children))
    return ParentNode("ul", list_items)

def ol_to_html_node(block: str) -> ParentNode:
    list_lines = block.split("\n")
    list_items = []
    for line in list_lines:
        line_without_prefix = line[3:]
        children = text_to_children(line_without_prefix)
        list_items.append(ParentNode("li", children))
    return ParentNode("ol", list_items)



