import os
from extract_title import extract_title
from blocks import markdown_to_html_node

# to_path will be something like /public/index.html
def generate_page(from_path: str, dst_path: str, template_path: str):
    print(f"Generating page from {from_path} to {dst_path} with template {template_path}")
    try:
        with open(from_path, "r", encoding="utf-8") as f:
            markdown = f.read()
        f.close()
    except FileNotFoundError:
        print(f"markdown file {from_path} not found")
        return
    try:
        with open(template_path, "r", encoding="utf-8") as f:
            template = f.read()
        f.close()
    except FileNotFoundError:
        print(f"template {template_path} not found")
        return
    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    dst_dir = os.path.dirname(dst_path)
    if not os.path.exists(dst_dir) or not os.path.isdir(dst_dir):
        os.makedirs(dst_dir)
    try:
        with open(dst_path, "w", encoding="utf-8") as f:
            f.write(template.replace("{{ title }}", title).replace("{{ content }}", content))
    except Exception as e:
        print(f"Error writing to {dst_path}: {e}")
        return
    
def generate_pages_recursively(dir_path_content: str, template_path: str, dest_dir_path:str):
    if not os.path.exists(dest_dir_path) or not os.path.isdir(dest_dir_path):
        os.makedirs(dest_dir_path)
    if not os.path.exists(dir_path_content) or not os.path.isdir(dir_path_content):
        raise ValueError(f"Directory {dir_path_content} does not exist")
    dir_list = os.listdir(dir_path_content)
    for file in dir_list:
        if file.endswith(".md"):
            generate_page(os.path.join(dir_path_content, file), os.path.join(dest_dir_path, file.replace(".md", ".html")), template_path)
        else:
            generate_pages_recursively(os.path.join(dir_path_content, file), template_path, os.path.join(dest_dir_path, file))
                
           
        