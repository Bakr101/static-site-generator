from enum import Enum
from htmlnode import LeafNode, ParentNode, HTMLNode
from textnode import text_node_to_html_node
from text_conversion import text_to_textnodes

def markdown_to_blocks(markdown: str) -> list[str]:
    split_markdown = markdown.split("\n\n")
    blocks = []
    for block in split_markdown:
      if block == "":
         continue
      block = block.strip()
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

def blocks_to_block_type(block: str) -> BlockType:
    #check if it's a heading
    if block.startswith("#"):
       #which heading level
       heading_level = 0
       for char in block:
           if char == "#":
               heading_level += 1
           else:
               break
       return BlockType(f"heading_{heading_level}")
    #check if it's a code block
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    #check if it's a quote
    elif block.startswith(">"):
        quote_lines = block.split("\n")
        valid_quote_lines = 0
        for line in quote_lines:
            if line.startswith(">"):
                valid_quote_lines += 1
            else:
                break
        if valid_quote_lines == len(quote_lines):
            return BlockType.QUOTE
        else:
            return BlockType.PARAGRAPH
    #check if it's an unordered list
    elif block.startswith("*") or block.startswith("-"):
        list_lines = block.split("\n")
        valid_list_lines = 0
        for line in list_lines:
            if line.startswith("*") or line.startswith("-"):
                valid_list_lines += 1
            else:
                break
        if valid_list_lines == len(list_lines):
            return BlockType.UNORDERED_LIST
        else:
            return BlockType.PARAGRAPH
    #check if it's an ordered list
    elif block.startswith("1. "):
        list_lines = block.split("\n")
        valid_list_lines = 0
        for line in list_lines:
            if line.startswith(f"{valid_list_lines+1}. "):
                valid_list_lines += 1
            else:
                break
        if valid_list_lines == len(list_lines):
            return BlockType.ORDERED_LIST
        else:
            return BlockType.PARAGRAPH
    else:
        return BlockType.PARAGRAPH

def markdown_to_html(markdown: str) -> HTMLNode:
    #split markdown to blocks
    parent_div = HTMLNode("div")
    blocks = markdown_to_blocks(markdown)\
    #loop over blocks
    # determine block type
    #based on block type, create html node with proper data
    for block in blocks:
        children  = text_to_children(block)


def text_to_children(text: str) -> list[HTMLNode]:
    children = []
    block_type = blocks_to_block_type(text)
    if block_type == BlockType.PARAGRAPH:
        children.append(LeafNode("p", text))
    elif block_type == BlockType.HEADING_1 or block_type == BlockType.HEADING_2 or block_type == BlockType.HEADING_3 or block_type == BlockType.HEADING_4 or block_type == BlockType.HEADING_5 or block_type == BlockType.HEADING_6:
        heading_level = text.count("#")
        children.append(LeafNode(f"h{heading_level}", text))
    elif block_type == BlockType.CODE:
        pre_tag = code_to_html(text)
        children.append(pre_tag)
    elif block_type == BlockType.QUOTE:
        quote_tag = blockquote_to_html(text)
        children.append(quote_tag)
    elif block_type == BlockType.UNORDERED_LIST:
        ul_tag = ul_to_html(text)
        children.append(ul_tag)
    elif block_type == BlockType.ORDERED_LIST:
        ol_tag = ol_to_html(text)
        children.append(ol_tag)
    return children
    
    
    

def blockquote_to_html(text: str) -> LeafNode:
    text_lines = text.split("\n")
    text_tags = []
    full_text = ""
    for line in text_lines:
        line = line.removeprefix(">")
        line = line.strip()
        full_text += line + "\n"
        
    text_nodes = text_to_textnodes(full_text)
    for text_node in text_nodes:
        text_tags = text_node_to_html_node(text_node)
        text_tags.append(text_tags)
    return LeafNode("blockquote", text_tags)


            
def code_to_html(text: str) -> ParentNode:
    remove_code_block_prefix = text.removeprefix("```")
    remove_code_block_suffix = remove_code_block_prefix.removesuffix("```")
    code_tag = LeafNode("code", remove_code_block_suffix)
    pre_tag = ParentNode("pre", [code_tag])
    return pre_tag

def ul_to_html(text: str) -> ParentNode:
    list_lines = text.split("\n")
    list_items = []
    for line in list_lines:
        line_without_prefix = line.removeprefix("*")
        line_without_prefix = line_without_prefix.removeprefix("-")
        line_without_prefix = line_without_prefix.strip()
        list_items.append(LeafNode("li", line_without_prefix))
    return ParentNode("ul", list_items)

def ol_to_html(text: str) -> ParentNode:
    list_lines = text.split("\n")
    list_items = []
    list_number = 1
    for line in list_lines:
        line_without_prefix = line.removeprefix(f"{list_number}. ")
        line_without_prefix = line_without_prefix.strip()
        list_items.append(LeafNode("li", line_without_prefix))
        list_number += 1
    return ParentNode("ol", list_items)



